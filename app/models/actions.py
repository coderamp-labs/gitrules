from pydantic import BaseModel
from typing import Dict, List, Any

class Agent(BaseModel):
    name: str
    filename: str

class Rule(BaseModel):
    name: str
    filename: str

class MCP(BaseModel):
    name: str
    config: Dict[str, Any]  # JSON configuration from mcps.json

class ActionsResponse(BaseModel):
    agents: List[Agent]
    rules: List[Rule]
    mcps: List[MCP]