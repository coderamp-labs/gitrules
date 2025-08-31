import yaml
from typing import List, Dict, Any, Optional
from pathlib import Path
from app.models.actions import Agent, Rule, MCP, Pack, Action, ActionType
from loguru import logger

class ActionsLoader:
    def __init__(self):
        self.actions_dir = Path(__file__).parent.parent / "actions"
        self.actions: List[Action] = []
        # Keep legacy lists for backward compatibility
        self.agents: List[Agent] = []
        self.rules: List[Rule] = []
        self.mcps: List[MCP] = []
        self.packs: List[Pack] = []
        logger.info(f"Loading actions from {self.actions_dir}")
        self.load_all()
    
    def load_all(self):
        """Load all actions from consolidated YAML files"""
        self.load_agents()
        self.load_rules()
        self.load_mcps()
        self.load_packs()
    
    def load_agents(self):
        """Load all agents from agents.yaml"""
        agents_file = self.actions_dir / "agents.yaml"
        if agents_file.exists():
            try:
                with open(agents_file, 'r') as f:
                    data = yaml.safe_load(f)
                    if data and 'agents' in data:
                        logger.info(f"Loading {len(data['agents'])} agents")
                        for agent_data in data['agents']:
                            slug = agent_data.get('slug', '')
                            # Create Action object
                            action = Action(
                                id=slug,
                                name=slug,
                                display_name=agent_data.get('display_name'),
                                action_type=ActionType.AGENT,
                                tags=agent_data.get('tags', []),
                                content=agent_data.get('content'),
                                filename=f"{slug}.md"
                            )
                            self.actions.append(action)
                            
                            # Also create legacy Agent for backward compatibility
                            self.agents.append(Agent(
                                name=slug,
                                filename=f"{slug}.md",
                                display_name=agent_data.get('display_name'),
                                slug=slug,
                                content=agent_data.get('content'),
                                tags=agent_data.get('tags', [])
                            ))
            except Exception as e:
                logger.error(f"Error loading agents from {agents_file}: {e}")
                self.agents = []
        else:
            logger.warning(f"Agents file not found: {agents_file}")
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
                        
                        # Create Action object
                        rule_type = ActionType.RULESET if rule_data.get('type') == 'ruleset' else ActionType.RULE
                        action = Action(
                            id=slug,
                            name=slug,
                            display_name=rule_data.get('display_name'),
                            action_type=rule_type,
                            tags=rule_data.get('tags'),
                            content=rule_data.get('content'),
                            author=rule_data.get('author'),
                            children=rule_data.get('children'),
                            filename=f"{slug}.yaml",
                            namespace=rule_data.get('namespace')
                        )
                        self.actions.append(action)
        else:
            self.rules = []
    
    def load_mcps(self):
        """Load all MCPs from mcps.yaml"""
        mcps_file = self.actions_dir / "mcps.yaml"
        if mcps_file.exists():
            with open(mcps_file, 'r') as f:
                data = yaml.safe_load(f)
                if data and 'mcps' in data:
                    for mcp_data in data['mcps']:
                        name = mcp_data.get('slug', '')
                        # Create Action object
                        action = Action(
                            id=name,
                            name=name,
                            display_name=mcp_data.get('display_name'),
                            action_type=ActionType.MCP,
                            tags=mcp_data.get('tags', []),
                            config=mcp_data.get('config', {}),
                            description=mcp_data.get('description')
                        )
                        self.actions.append(action)
                        
                        # Also create legacy MCP for backward compatibility
                        self.mcps.append(MCP(
                            name=name,
                            config=mcp_data.get('config', {}),
                            tags=mcp_data.get('tags', []),
                            description=mcp_data.get('description')
                        ))
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
    
    def load_packs(self):
        """Load all packs from packs.yaml"""
        packs_file = self.actions_dir / "packs.yaml"
        if packs_file.exists():
            with open(packs_file, 'r') as f:
                data = yaml.safe_load(f)
                if data and 'packs' in data:
                    for pack_data in data['packs']:
                        pack_id = pack_data.get('id', '')
                        # Create Action object
                        action = Action(
                            id=pack_id,
                            name=pack_data.get('name', ''),
                            display_name=pack_data.get('display_name'),
                            action_type=ActionType.PACK,
                            tags=pack_data.get('tags', []),
                            children=pack_data.get('actions', [])
                        )
                        self.actions.append(action)
                        
                        # Also create Pack for backward compatibility
                        self.packs.append(Pack(
                            id=pack_id,
                            name=pack_data.get('name', ''),
                            display_name=pack_data.get('display_name'),
                            tags=pack_data.get('tags', []),
                            description=pack_data.get('description'),
                            actions=pack_data.get('actions', [])
                        ))
        else:
            self.packs = []
    
    def get_packs(self) -> List[Pack]:
        """Get all packs"""
        return self.packs
    
    def get_actions(self, action_type: Optional[ActionType] = None, tags: Optional[List[str]] = None, 
                   limit: int = 30, offset: int = 0) -> List[Action]:
        """Get all actions with optional filtering"""
        filtered = self.actions
        
        # Filter by action type
        if action_type:
            filtered = [a for a in filtered if a.action_type == action_type]
        
        # Filter by tags
        if tags:
            filtered = [a for a in filtered if a.tags and any(tag in a.tags for tag in tags)]
        
        # Apply pagination
        return filtered[offset:offset + limit]
    
    def get_action_by_id(self, action_id: str) -> Optional[Action]:
        """Get a specific action by ID"""
        return next((a for a in self.actions if a.id == action_id), None)
    
    def get_agent(self, action_id: str) -> Optional[Dict[str, Any]]:
        """Get agent data by ID for legacy compatibility"""
        action = self.get_action_by_id(action_id)
        if action and action.action_type == ActionType.AGENT:
            return {
                'name': action.name,
                'display_name': action.display_name,
                'slug': action.id,
                'filename': action.filename,
                'content': action.content,
                'tags': action.tags
            }
        return None
    
    def get_rule(self, action_id: str) -> Optional[Dict[str, Any]]:
        """Get rule data by ID for legacy compatibility"""
        action = self.get_action_by_id(action_id)
        if action and action.action_type in [ActionType.RULE, ActionType.RULESET]:
            return {
                'name': action.name,
                'display_name': action.display_name,
                'slug': action.id,
                'content': action.content,
                'tags': action.tags,
                'type': action.action_type.value.lower()
            }
        return None
    
    def get_mcp(self, action_id: str) -> Optional[Dict[str, Any]]:
        """Get MCP data by ID for legacy compatibility"""
        action = self.get_action_by_id(action_id)
        if action and action.action_type == ActionType.MCP:
            return {
                'name': action.name,
                'display_name': action.display_name,
                'slug': action.id,
                'config': action.config,
                'tags': action.tags,
                'description': action.description
            }
        return None

# Create singleton instance
actions_loader = ActionsLoader()