import os
import json
from typing import List, Dict, Any
from pathlib import Path
from app.models.actions import Agent, Rule, MCP

class ActionsLoader:
    def __init__(self):
        self.actions_dir = Path(__file__).parent.parent / "actions"
        self.agents: List[Agent] = []
        self.rules: List[Rule] = []
        self.mcps: List[MCP] = []
        self.load_all()
    
    def load_all(self):
        """Load all actions on initialization"""
        self.load_agents()
        self.load_rules()
        self.load_mcps()
    
    def load_agents(self):
        """Load all agent files from actions/agents directory"""
        agents_dir = self.actions_dir / "agents"
        if agents_dir.exists():
            self.agents = []
            for file_path in agents_dir.glob("*.md"):
                name = file_path.stem.replace('-', ' ').title()
                self.agents.append(Agent(
                    name=name,
                    filename=file_path.name
                ))
    
    def load_rules(self):
        """Load all rule files from actions/rules directory"""
        rules_dir = self.actions_dir / "rules"
        if rules_dir.exists():
            self.rules = []
            for file_path in rules_dir.glob("*.md"):
                name = file_path.stem.replace('-', ' ').title()
                self.rules.append(Rule(
                    name=name,
                    filename=file_path.name
                ))
    
    def load_mcps(self):
        """Load MCPs from actions/mcps.json"""
        mcps_file = self.actions_dir / "mcps.json"
        if mcps_file.exists():
            with open(mcps_file, 'r') as f:
                mcps_data = json.load(f)
                self.mcps = [
                    MCP(name=name, config=config)
                    for name, config in mcps_data.items()
                ]
    
    def get_all(self) -> Dict[str, Any]:
        """Get all loaded actions"""
        return {
            "agents": self.agents,
            "rules": self.rules,
            "mcps": self.mcps
        }
    
    def get_agents(self) -> List[Agent]:
        """Get all agents"""
        return self.agents
    
    def get_rules(self) -> List[Rule]:
        """Get all rules"""
        return self.rules
    
    def get_mcps(self) -> List[MCP]:
        """Get all MCPs"""
        return self.mcps

# Create singleton instance
actions_loader = ActionsLoader()