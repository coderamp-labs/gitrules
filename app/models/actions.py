from pydantic import BaseModel
from typing import Dict, List, Any, Optional
from enum import Enum

class ActionType(str, Enum):
    AGENT = "agent"
    RULE = "rule"
    RULESET = "ruleset"
    MCP = "mcp"
    PACK = "pack"

class Action(BaseModel):
    """Action model that can represent any type of action"""
    id: str  # Unique identifier (slug for agents/rules, name for MCPs)
    name: str
    display_name: Optional[str] = None
    action_type: ActionType
    tags: Optional[List[str]] = None
    content: Optional[str] = None  # For agents/rules
    config: Optional[Dict[str, Any]] = None  # For MCPs
    author: Optional[str] = None  # For rules
    children: Optional[List[str]] = None  # For rulesets and packs
    filename: Optional[str] = None  # For agents/rules
    namespace: Optional[str] = None  # For rules

class Agent(BaseModel):
    name: str  # For backward compatibility
    filename: str
    display_name: Optional[str] = None
    slug: Optional[str] = None
    content: Optional[str] = None
    tags: Optional[List[str]] = None

class Rule(BaseModel):
    name: str  # For backward compatibility
    filename: str
    display_name: Optional[str] = None
    slug: Optional[str] = None
    content: Optional[str] = None
    author: Optional[str] = None
    tags: Optional[List[str]] = None
    children: Optional[List[str]] = None  # List of rule IDs
    type: str = "rule"  # "rule" or "ruleset"
    namespace: Optional[str] = None

class MCP(BaseModel):
    name: str
    config: Dict[str, Any]  # JSON configuration from mcps.json
    tags: Optional[List[str]] = None

class Pack(BaseModel):
    """A pack is a collection of other actions"""
    id: str
    name: str
    display_name: Optional[str] = None
    tags: Optional[List[str]] = None
    description: Optional[str] = None
    actions: List[str]  # List of action IDs
    
class ActionsResponse(BaseModel):
    agents: List[Agent]
    rules: List[Rule]
    mcps: List[MCP]
    
class ActionsListResponse(BaseModel):
    actions: List[Action]
    total: int
    has_more: bool