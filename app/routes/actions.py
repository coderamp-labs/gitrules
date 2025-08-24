from fastapi import APIRouter, HTTPException, Body, Query
from app.models.actions import ActionsResponse, Agent, Rule, MCP
from app.services.actions_loader import actions_loader
from app.services.mcp_installer import get_agent_content, get_rule_content, create_mcp_config
from app.services.search_service import search_service
from typing import List, Dict, Any, Optional
import json

router = APIRouter(prefix="/api", tags=["actions"])

@router.get("/actions", response_model=ActionsResponse, operation_id="get_all_actions_endpoint")
async def get_all_actions():
    """Get all available actions (agents, rules, MCPs)"""
    return ActionsResponse(
        agents=actions_loader.get_agents(),
        rules=actions_loader.get_rules(),
        mcps=actions_loader.get_mcps()
    )

@router.get("/agents", operation_id="get_agents_endpoint")
async def get_agents(
    after: Optional[str] = Query(None, description="Cursor for pagination (use slug of last item from previous page)"),
    limit: int = Query(30, ge=1, le=30, description="Maximum number of results (max 30)")
):
    """Get available agents with tags only, limited to 30 items"""
    agents = actions_loader.get_agents()
    
    # Find starting position if 'after' is provided
    start_idx = 0
    if after:
        for idx, agent in enumerate(agents):
            if agent.slug == after:
                start_idx = idx + 1
                break
    
    # Apply limit
    paginated_agents = agents[start_idx:start_idx + limit]
    
    return [
        {
            "name": agent.name,
            "display_name": agent.display_name,
            "slug": agent.slug,
            "tags": agent.tags,
            "filename": agent.filename
        }
        for agent in paginated_agents
    ]

@router.get("/rules", operation_id="get_rules_endpoint")
async def get_rules(
    after: Optional[str] = Query(None, description="Cursor for pagination (use slug of last item from previous page)"),
    limit: int = Query(30, ge=1, le=30, description="Maximum number of results (max 30)")
):
    """Get available rules with tags only, limited to 30 items"""
    rules = actions_loader.get_rules()
    
    # Find starting position if 'after' is provided
    start_idx = 0
    if after:
        for idx, rule in enumerate(rules):
            if rule.slug == after:
                start_idx = idx + 1
                break
    
    # Apply limit
    paginated_rules = rules[start_idx:start_idx + limit]
    
    return [
        {
            "name": rule.name,
            "display_name": rule.display_name,
            "slug": rule.slug,
            "tags": rule.tags,
            "filename": rule.filename
        }
        for rule in paginated_rules
    ]

@router.get("/mcps", operation_id="get_mcps_endpoint")
async def get_mcps(
    after: Optional[str] = Query(None, description="Cursor for pagination (use name of last item from previous page)"),
    limit: int = Query(30, ge=1, le=30, description="Maximum number of results (max 30)")
):
    """Get available MCPs with tags only, limited to 30 items"""
    mcps = actions_loader.get_mcps()
    
    # Find starting position if 'after' is provided
    start_idx = 0
    if after:
        for idx, mcp in enumerate(mcps):
            if mcp.name == after:
                start_idx = idx + 1
                break
    
    # Apply limit
    paginated_mcps = mcps[start_idx:start_idx + limit]
    
    return [
        {
            "name": mcp.name,
            "tags": mcp.tags if hasattr(mcp, 'tags') else []
        }
        for mcp in paginated_mcps
    ]




@router.get("/merged-block", operation_id="get_merged_actions_block_endpoint")
async def get_merged_actions_block():
    """Get all actions merged into a single block with metadata for frontend"""
    agents = actions_loader.get_agents()
    rules = actions_loader.get_rules()
    mcps = actions_loader.get_mcps()
    
    # Build merged block with all actions and their metadata
    merged = {
        "agents": [
            {
                "display_name": agent.display_name or agent.name,
                "slug": agent.slug or agent.filename.replace('.yaml', '').replace('.md', ''),
                "content": agent.content or get_agent_content(agent.filename),
                "filename": agent.filename
            }
            for agent in agents
        ],
        "rules": [
            {
                "display_name": rule.display_name or rule.name,
                "slug": rule.slug or rule.filename.replace('.yaml', '').replace('.md', ''),
                "content": rule.content or get_rule_content(rule.filename),
                "filename": rule.filename
            }
            for rule in rules
        ],
        "mcps": [
            {
                "name": mcp.name,
                "config": mcp.config
            }
            for mcp in mcps
        ]
    }
    
    return merged

@router.get("/search/agents", tags=["mcp"], operation_id="search_agents_endpoint")
async def search_agents(
    query: str = Query(..., description="Search query. Supports wildcards: * (any characters) and ? (single character)"),
    limit: int = Query(10, ge=1, le=100, description="Maximum number of results")
):
    """Search for agents by name, display_name, or content. Supports wildcard patterns with * and ?"""
    results = search_service.search_agents(query, limit)
    return {"results": results}

@router.get("/search/rules", tags=["mcp"], operation_id="search_rules_endpoint")
async def search_rules(
    query: str = Query(..., description="Search query. Supports wildcards: * (any characters) and ? (single character)"),
    limit: int = Query(10, ge=1, le=100, description="Maximum number of results")
):
    """Search for rules by name, display_name, content, tags, or author. Supports wildcard patterns with * and ?"""
    results = search_service.search_rules(query, limit)
    return {"results": results}

@router.get("/search/mcps", tags=["mcp"], operation_id="search_mcps_endpoint")
async def search_mcps(
    query: str = Query(..., description="Search query. Supports wildcards: * (any characters) and ? (single character)"),
    limit: int = Query(10, ge=1, le=100, description="Maximum number of results")
):
    """Search for MCPs by name or config content. Supports wildcard patterns with * and ?"""
    results = search_service.search_mcps(query, limit)
    return {"results": results}

@router.get("/search", tags=["mcp"], operation_id="search_all_endpoint")
async def search_all(
    query: str = Query(..., description="Search query. Supports wildcards: * (any characters) and ? (single character)"),
    limit: int = Query(10, ge=1, le=100, description="Maximum number of results per category")
):
    """Search across all types (agents, rules, MCPs). Supports wildcard patterns with * and ?"""
    return search_service.search_all(query, limit)

@router.get("/rules/{rule_ids}", tags=["mcp"], operation_id="get_multiple_rules_content")
async def get_multiple_rules_content(rule_ids: str):
    """Get content for multiple rules by comma-separated IDs/slugs"""
    ids = [id.strip() for id in rule_ids.split(',') if id.strip()]
    
    if not ids:
        raise HTTPException(status_code=400, detail="No rule IDs provided")
    
    rules = actions_loader.get_rules()
    results = []
    
    for rule_id in ids:
        # Match by slug first, fallback to name for backward compat
        rule = next((r for r in rules if (r.slug == rule_id or r.name == rule_id)), None)
        
        if rule:
            results.append({
                "id": rule_id,
                "slug": rule.slug,
                "name": rule.name,
                "display_name": rule.display_name,
                "content": rule.content,
                "filename": rule.filename
            })
        else:
            results.append({
                "id": rule_id,
                "error": f"Rule not found: {rule_id}"
            })
    
    return {"rules": results}

@router.get("/agents/{agent_ids}", tags=["mcp"], operation_id="get_multiple_agents_content")
async def get_multiple_agents_content(agent_ids: str):
    """Get content for multiple agents by comma-separated IDs/slugs"""
    ids = [id.strip() for id in agent_ids.split(',') if id.strip()]
    
    if not ids:
        raise HTTPException(status_code=400, detail="No agent IDs provided")
    
    agents = actions_loader.get_agents()
    results = []
    
    for agent_id in ids:
        # Match by slug first, fallback to name for backward compat
        agent = next((a for a in agents if (a.slug == agent_id or a.name == agent_id)), None)
        
        if agent:
            results.append({
                "id": agent_id,
                "slug": agent.slug,
                "name": agent.name,
                "display_name": agent.display_name,
                "content": agent.content,
                "filename": agent.filename
            })
        else:
            results.append({
                "id": agent_id,
                "error": f"Agent not found: {agent_id}"
            })
    
    return {"agents": results}

@router.get("/mcps/{mcp_ids}", tags=["mcp"], operation_id="get_multiple_mcps_config")
async def get_multiple_mcps_config(mcp_ids: str):
    """Get config for multiple MCPs by comma-separated names. These MCPs will need to be installed on the client side (e.g. in `.mcp.json`)"""
    ids = [id.strip() for id in mcp_ids.split(',') if id.strip()]
    
    if not ids:
        raise HTTPException(status_code=400, detail="No MCP IDs provided")
    
    mcps = actions_loader.get_mcps()
    results = []
    
    for mcp_id in ids:
        # Match by name
        mcp = next((m for m in mcps if m.name == mcp_id), None)
        
        if mcp:
            results.append({
                "id": mcp_id,
                "name": mcp.name,
                "config": mcp.config
            })
        else:
            results.append({
                "id": mcp_id,
                "error": f"MCP not found: {mcp_id}"
            })
    
    return {"mcps": results}