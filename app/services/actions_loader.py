import yaml
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
        """Load all actions from consolidated YAML files"""
        self.load_agents()
        self.load_rules()
        self.load_mcps()
    
    def load_agents(self):
        """Load all agents from agents.yaml"""
        agents_file = self.actions_dir / "agents.yaml"
        if agents_file.exists():
            with open(agents_file, 'r') as f:
                data = yaml.safe_load(f)
                if data and 'agents' in data:
                    self.agents = [
                        Agent(
                            name=agent.get('slug', ''),  # Use slug as name for backward compat
                            filename=f"{agent.get('slug', '')}.yaml",  # Virtual filename
                            display_name=agent.get('display_name'),
                            slug=agent.get('slug'),
                            content=agent.get('content')
                        )
                        for agent in data['agents']
                    ]
        else:
            self.agents = []
    
    def _parse_rule(self, slug: str, rule_data: Dict[str, Any]) -> Rule:
        """Parse a single rule or ruleset from the YAML data"""
        rule = Rule(
            name=slug,  # Use slug as name for backward compat
            filename=f"{slug}.yaml",  # Virtual filename
            display_name=rule_data.get('display_name'),
            slug=slug,
            content=rule_data.get('content'),
            author=rule_data.get('author'),
            tags=rule_data.get('tags'),
            type=rule_data.get('type', 'rule'),
            namespace=rule_data.get('namespace'),
            children=rule_data.get('children')  # Now just a list of rule IDs
        )
        
        return rule
    
    def load_rules(self):
        """Load all rules from rules.yaml"""
        rules_file = self.actions_dir / "rules.yaml"
        if rules_file.exists():
            with open(rules_file, 'r') as f:
                data = yaml.safe_load(f)
                if data:
                    self.rules = []
                    # Now the top-level keys are the slugs
                    for slug, rule_data in data.items():
                        rule = self._parse_rule(slug, rule_data)
                        self.rules.append(rule)
        else:
            self.rules = []
    
    def load_mcps(self):
        """Load all MCPs from mcps.yaml"""
        mcps_file = self.actions_dir / "mcps.yaml"
        if mcps_file.exists():
            with open(mcps_file, 'r') as f:
                data = yaml.safe_load(f)
                if data and 'mcps' in data:
                    self.mcps = [
                        MCP(
                            name=mcp.get('slug', ''),
                            config=mcp.get('config', {})
                        )
                        for mcp in data['mcps']
                    ]
        else:
            self.mcps = []
    
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
    
    def get_agent_by_slug(self, slug: str) -> Agent:
        """Get a specific agent by slug"""
        return next((a for a in self.agents if a.slug == slug), None)
    
    def get_rule_by_slug(self, slug: str) -> Rule:
        """Get a specific rule by slug"""
        return next((r for r in self.rules if r.slug == slug), None)

# Create singleton instance
actions_loader = ActionsLoader()