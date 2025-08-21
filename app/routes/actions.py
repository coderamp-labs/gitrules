from fastapi import APIRouter, HTTPException, Body
from app.models.actions import ActionsResponse, Agent, Rule, MCP
from app.services.actions_loader import actions_loader
from app.services.mcp_installer import get_agent_content, create_mcp_config
from typing import List, Dict, Any

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

@router.get("/agent-content/{agent_name}")
async def get_agent_content_endpoint(agent_name: str):
    """Get agent content for virtual workspace"""
    agents = actions_loader.get_agents()
    agent = next((a for a in agents if a.name == agent_name), None)
    
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    
    content = get_agent_content(agent.filename)
    if not content:
        raise HTTPException(status_code=500, detail="Failed to read agent file")
    
    return {
        "filename": agent.filename,
        "content": content,
        "path": f".claude/agents/{agent.filename}"
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