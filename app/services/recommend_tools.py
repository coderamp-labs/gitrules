"""
Service for recommending tools based on repository context.
"""

import json
import hashlib
from typing import Dict, List, Tuple, Optional, Any
from app.services.actions_loader import actions_loader
import httpx
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


def build_tools_catalog() -> Dict[str, List[Dict[str, Any]]]:
    """
    Build a minimal catalog of available tools from actions_loader.
    
    Returns:
        Dictionary with three lists: agents, rules, mcps
        Each item has: slug, display_name, tags (optional), type (for rules)
    """
    catalog = {
        "agents": [],
        "rules": [],
        "mcps": []
    }
    
    # Get agents
    for agent in actions_loader.get_agents():
        catalog["agents"].append({
            "slug": agent.slug or agent.name,
            "display_name": agent.display_name or agent.name,
            "tags": getattr(agent, 'tags', []) or []
        })
    
    # Get rules
    for rule in actions_loader.get_rules():
        catalog["rules"].append({
            "slug": rule.slug or rule.name,
            "display_name": rule.display_name or rule.name,
            "type": rule.type,  # 'rule' or 'ruleset'
            "tags": getattr(rule, 'tags', []) or []
        })
    
    # Get MCPs (note: MCP uses 'name' as identifier)
    for mcp in actions_loader.get_mcps():
        catalog["mcps"].append({
            "slug": mcp.name,  # MCPs use 'name' as slug
            "display_name": mcp.name,
            "tags": []  # MCPs don't have tags in current structure
        })
    
    # Sort by slug for stability
    catalog["agents"].sort(key=lambda x: x["slug"])
    catalog["rules"].sort(key=lambda x: x["slug"])
    catalog["mcps"].sort(key=lambda x: x["slug"])
    
    return catalog


def get_catalog_version(catalog: Dict[str, List[Dict[str, Any]]]) -> str:
    """
    Calculate a stable hash of the catalog slugs.
    
    Args:
        catalog: The tools catalog
        
    Returns:
        SHA1 hash of concatenated sorted slugs
    """
    all_slugs = []
    all_slugs.extend([a["slug"] for a in catalog["agents"]])
    all_slugs.extend([r["slug"] for r in catalog["rules"]])
    all_slugs.extend([m["slug"] for m in catalog["mcps"]])
    
    slug_string = ",".join(sorted(all_slugs))
    return hashlib.sha1(slug_string.encode()).hexdigest()[:8]


def format_catalog_for_prompt(catalog: Dict[str, List[Dict[str, Any]]]) -> str:
    """
    Format the catalog into a compact text for the LLM prompt.
    
    Args:
        catalog: The tools catalog
        
    Returns:
        Formatted string with one line per tool
    """
    lines = []
    
    # Format agents
    lines.append("- Agents:")
    for agent in catalog["agents"]:
        tags = f" — [{', '.join(agent['tags'])}]" if agent.get('tags') else ""
        lines.append(f"  {agent['slug']} — {agent['display_name']}{tags}")
    
    # Format rules
    lines.append("- Rules:")
    for rule in catalog["rules"]:
        tags = f" — [{', '.join(rule['tags'])}]" if rule.get('tags') else ""
        lines.append(f"  {rule['slug']} — {rule['display_name']} — {rule['type']}{tags}")
    
    # Format MCPs
    lines.append("- MCPs:")
    for mcp in catalog["mcps"]:
        tags = f" — [{', '.join(mcp['tags'])}]" if mcp.get('tags') else ""
        lines.append(f"  {mcp['slug']} — {mcp['display_name']}{tags}")
    
    return "\n".join(lines)


def call_llm_for_reco(context: str, catalog_text: str, user_prompt: str = "", api_key: Optional[str] = None) -> str:
    """
    Call the LLM to get tool recommendations.
    
    Args:
        context: Repository context (summary + tree + content)
        catalog_text: Formatted catalog of available tools
        user_prompt: Optional user guidance
        api_key: Optional OpenAI API key
        
    Returns:
        Raw LLM response string
    """
    # Get API key
    if not api_key:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found")
    
    # System prompt
    system_prompt = """You are "Tool Recommender for Codebases." Your job is to read a repository context and choose a minimal set of helpful tools (rules, agents, MCPs) from the provided catalog.

Hard requirements:
- Output strictly valid JSON. No markdown, no commentary.
- Use only the slugs present in the catalog below.
- Prefer minimal selections: 0–2 per category (maximum 3).
- If unsure, return empty arrays.

Selection guidelines:
- Pick items that improve correctness, safety, or developer workflow for this codebase.
- Avoid redundant overlap (e.g., don't pick both a ruleset and all its child rules).
- Skip "fun/novelty" items unless clearly beneficial.
- Base the decision solely on the given repository context and the catalog.

Catalog (one line per item, slug first):
""" + catalog_text + """

Return JSON with this exact shape:
- rules: array of slugs
- agents: array of slugs
- mcps: array of slugs
- rationales (optional): object whose keys are "rules:<slug>", "agents:<slug>", "mcps:<slug>" and whose values are short one-line reasons.

You will now receive the repository context (summary, tree, truncated content) and an optional user focus. Choose minimal helpful tools from the catalog and return JSON only."""

    # User message
    user_message = "Here is the codebase context (truncated). Choose minimal useful tools from the catalog above.\n\n"
    user_message += context
    if user_prompt:
        user_message += f"\n\nUser focus: {user_prompt}"
    
    # Prepare request
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]
    
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "gpt-4o-mini",
        "messages": messages,
        "temperature": 0.2,  # Low temperature for consistency
        "max_tokens": 1000
    }
    
    try:
        with httpx.Client(timeout=60.0) as client:
            response = client.post(url, json=data, headers=headers)
            response.raise_for_status()
            result = response.json()
            
            # Extract the content
            content = result["choices"][0]["message"]["content"]
            return content
            
    except Exception as e:
        raise Exception(f"LLM call failed: {str(e)}")


def parse_and_validate(llm_raw: str, catalog: Dict[str, List[Dict[str, Any]]]) -> Tuple[Dict[str, List[str]], Optional[Dict[str, str]]]:
    """
    Parse and validate the LLM response against the catalog.
    
    Args:
        llm_raw: Raw JSON string from LLM
        catalog: The tools catalog for validation
        
    Returns:
        Tuple of (preselect dict, rationales dict or None)
    """
    # Try to parse JSON
    try:
        data = json.loads(llm_raw)
    except json.JSONDecodeError:
        # Try to extract JSON from possible markdown or text
        import re
        json_match = re.search(r'\{[^{}]*\}', llm_raw, re.DOTALL)
        if json_match:
            try:
                data = json.loads(json_match.group())
            except:
                # Return empty if we can't parse
                return {"rules": [], "agents": [], "mcps": []}, None
        else:
            return {"rules": [], "agents": [], "mcps": []}, None
    
    # Extract valid slugs
    valid_agent_slugs = {a["slug"] for a in catalog["agents"]}
    valid_rule_slugs = {r["slug"] for r in catalog["rules"]}
    valid_mcp_slugs = {m["slug"] for m in catalog["mcps"]}
    
    # Filter and limit selections
    preselect = {
        "rules": [],
        "agents": [],
        "mcps": []
    }
    
    # Process rules (max 3, dedupe)
    if "rules" in data and isinstance(data["rules"], list):
        seen = set()
        for slug in data["rules"][:3]:  # Max 3
            if slug in valid_rule_slugs and slug not in seen:
                preselect["rules"].append(slug)
                seen.add(slug)
    
    # Process agents (max 3, dedupe)
    if "agents" in data and isinstance(data["agents"], list):
        seen = set()
        for slug in data["agents"][:3]:  # Max 3
            if slug in valid_agent_slugs and slug not in seen:
                preselect["agents"].append(slug)
                seen.add(slug)
    
    # Process MCPs (max 3, dedupe)
    if "mcps" in data and isinstance(data["mcps"], list):
        seen = set()
        for slug in data["mcps"][:3]:  # Max 3
            if slug in valid_mcp_slugs and slug not in seen:
                preselect["mcps"].append(slug)
                seen.add(slug)
    
    # Extract rationales if present
    rationales = None
    if "rationales" in data and isinstance(data["rationales"], dict):
        rationales = {}
        # Only keep rationales for selected items
        for key, value in data["rationales"].items():
            parts = key.split(":", 1)
            if len(parts) == 2:
                category, slug = parts
                if category == "rules" and slug in preselect["rules"]:
                    rationales[key] = str(value)[:200]  # Limit length
                elif category == "agents" and slug in preselect["agents"]:
                    rationales[key] = str(value)[:200]
                elif category == "mcps" and slug in preselect["mcps"]:
                    rationales[key] = str(value)[:200]
    
    return preselect, rationales