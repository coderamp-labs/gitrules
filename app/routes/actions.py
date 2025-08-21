from fastapi import APIRouter
from app.models.actions import ActionsResponse, Agent, Rule, MCP
from app.services.actions_loader import actions_loader
from typing import List

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