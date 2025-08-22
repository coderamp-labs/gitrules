from pydantic import BaseModel
from typing import Dict, List, Any, Optional

class Agent(BaseModel):
    name: str  # For backward compatibility
    filename: str
    display_name: Optional[str] = None
    slug: Optional[str] = None
    content: Optional[str] = None

class Rule(BaseModel):
    name: str  # For backward compatibility
    filename: str
    display_name: Optional[str] = None
    slug: Optional[str] = None
    content: Optional[str] = None

class MCP(BaseModel):
    name: str
    config: Dict[str, Any]  # JSON configuration from mcps.json

class ActionsResponse(BaseModel):
    agents: List[Agent]
    rules: List[Rule]
    mcps: List[MCP]