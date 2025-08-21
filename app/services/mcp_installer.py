import json
import re
from pathlib import Path
from typing import Dict, Any, Set, Tuple

def get_agent_content(agent_filename: str) -> str:
    """Get agent content from actions/agents directory"""
    source_path = Path(__file__).parent.parent / "actions" / "agents" / agent_filename
    if source_path.exists():
        with open(source_path, 'r') as f:
            return f.read()
    return ""

def get_current_mcp_config() -> Dict[str, Any]:
    """Get current .mcp.json config from virtual workspace or create new"""
    # This would be called from frontend with workspace content
    # For now, return default structure
    return {"mcpServers": {}}

def create_mcp_config(existing_config: Dict[str, Any], mcp_name: str, mcp_config: Dict[str, Any]) -> Tuple[str, bool]:
    """Create updated .mcp.json content, returns (content, was_removed)"""
    if not isinstance(existing_config, dict) or "mcpServers" not in existing_config:
        config = {"mcpServers": {}}
    else:
        config = existing_config.copy()
    
    # Toggle behavior: if exists, remove it; if not, add it
    was_removed = False
    if mcp_name in config["mcpServers"]:
        del config["mcpServers"][mcp_name]
        was_removed = True
    else:
        config["mcpServers"][mcp_name] = mcp_config
    
    return json.dumps(config, indent=2), was_removed

def extract_env_vars_from_config(config: Dict[str, Any]) -> Set[str]:
    """Extract environment variable names from MCP config"""
    env_vars = set()
    
    def find_env_vars(obj):
        if isinstance(obj, str):
            matches = re.findall(r'\$\{([^}]+)\}', obj)
            env_vars.update(matches)
        elif isinstance(obj, dict):
            for value in obj.values():
                find_env_vars(value)
        elif isinstance(obj, list):
            for item in obj:
                find_env_vars(item)
    
    find_env_vars(config)
    return env_vars