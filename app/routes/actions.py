from fastapi import APIRouter, HTTPException, Body
from app.models.actions import ActionsResponse, Agent, Rule, MCP
from app.services.actions_loader import actions_loader
from app.services.mcp_installer import get_agent_content, get_rule_content, create_mcp_config
from typing import List, Dict, Any
import json

router = APIRouter(prefix="/api/actions", tags=["actions"])

@router.get("/", response_model=ActionsResponse)
async def get_all_actions():
    """Get all available actions (agents, rules, MCPs)"""
    return ActionsResponse(
        agents=actions_loader.get_agents(),
        rules=actions_loader.get_rules(),
        mcps=actions_loader.get_mcps()
    )

@router.get("/agents", response_model=List[Agent])
async def get_agents():
    """Get all available agents"""
    return actions_loader.get_agents()

@router.get("/rules", response_model=List[Rule])
async def get_rules():
    """Get all available rules"""
    return actions_loader.get_rules()

@router.get("/mcps", response_model=List[MCP])
async def get_mcps():
    """Get all available MCPs"""
    return actions_loader.get_mcps()

@router.get("/agent-content/{agent_id}")
async def get_agent_content_endpoint(agent_id: str):
    """Get agent content for virtual workspace"""
    agents = actions_loader.get_agents()
    # Match by slug first, fallback to name for backward compat
    agent = next((a for a in agents if (a.slug == agent_id or a.name == agent_id)), None)
    
    if not agent:
        raise HTTPException(status_code=404, detail=f"Agent not found: {agent_id}")
    
    # Get content directly from the agent object (already loaded from consolidated file)
    content = agent.content
    if not content:
        raise HTTPException(status_code=500, detail="Agent has no content")
    
    return {
        "filename": agent.filename,
        "content": content,
        "path": f".claude/agents/{agent.filename}"
    }

@router.get("/rule-content/{rule_id}")
async def get_rule_content_endpoint(rule_id: str):
    """Get rule content to append to CLAUDE.md"""
    rules = actions_loader.get_rules()
    # Match by slug first, fallback to name for backward compat
    rule = next((r for r in rules if (r.slug == rule_id or r.name == rule_id)), None)
    
    if not rule:
        raise HTTPException(status_code=404, detail=f"Rule not found: {rule_id}")
    
    # Get content directly from the rule object (already loaded from consolidated file)
    content = rule.content
    if not content:
        raise HTTPException(status_code=500, detail="Rule has no content")
    
    return {
        "content": content.strip()
    }

@router.post("/mcp-config/{mcp_name}")
async def get_mcp_config_endpoint(mcp_name: str, current_config: Dict[str, Any] = Body(default={})):
    """Get updated MCP config for virtual workspace"""
    mcps = actions_loader.get_mcps()
    mcp = next((m for m in mcps if m.name == mcp_name), None)
    
    if not mcp:
        raise HTTPException(status_code=404, detail="MCP not found")
    
    updated_config, was_removed = create_mcp_config(current_config, mcp.name, mcp.config)
    
    return {
        "filename": ".mcp.json",
        "content": updated_config,
        "path": ".mcp.json",
        "was_removed": was_removed
    }

@router.get("/merged-block")
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