import json
import re
from typing import Dict, Any, Set, Tuple
from app.services.actions_loader import actions_loader

def get_agent_content(agent_identifier: str) -> str:
    """Get agent content from consolidated agents.yaml"""
    # Try to find by slug first, then by name for backward compat
    agent = actions_loader.get_agent_by_slug(agent_identifier)
    if not agent:
        # Fallback to finding by name
        agent = next((a for a in actions_loader.get_agents() if a.name == agent_identifier), None)
    
    if agent and agent.content:
        return agent.content
    return ""

def get_rule_content(rule_identifier: str) -> str:
    """Get rule content from consolidated rules.yaml"""
    # Try to find by slug first, then by name for backward compat
    rule = actions_loader.get_rule_by_slug(rule_identifier)
    if not rule:
        # Fallback to finding by name
        rule = next((r for r in actions_loader.get_rules() if r.name == rule_identifier), None)
    
    if rule and rule.content:
        return rule.content
    return ""

def get_current_mcp_config() -> Dict[str, Any]:
    """Get current .mcp.json config from virtual workspace or create new"""
    # This would be called from frontend with workspace content
    # For now, return default structure
    return {"mcpServers": {}}

def create_mcp_config(existing_config: Dict[str, Any], mcp_name: str, mcp_config: Dict[str, Any]) -> Tuple[str, bool]:
    """Create updated .mcp.json content, returns (content, was_removed)"""
    if not isinstance(existing_config, dict) or "mcpServers" not in existing_config:
        config = {"mcpServers": {}}
    else:
        config = existing_config.copy()
    
    # Toggle behavior: if exists, remove it; if not, add it
    was_removed = False
    if mcp_name in config["mcpServers"]:
        del config["mcpServers"][mcp_name]
        was_removed = True
    else:
        config["mcpServers"][mcp_name] = mcp_config
    
    return json.dumps(config, indent=2), was_removed

def extract_env_vars_from_config(config: Dict[str, Any]) -> Set[str]:
    """Extract environment variable names from MCP config"""
    env_vars = set()
    
    def find_env_vars(obj):
        if isinstance(obj, str):
            matches = re.findall(r'\$\{([^}]+)\}', obj)
            env_vars.update(matches)
        elif isinstance(obj, dict):
            for value in obj.values():
                find_env_vars(value)
        elif isinstance(obj, list):
            for item in obj:
                find_env_vars(item)
    
    find_env_vars(config)
    return env_vars