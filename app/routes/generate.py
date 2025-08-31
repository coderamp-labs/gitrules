from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import json
from app.services.actions_loader import actions_loader

router = APIRouter(prefix="/api", tags=["generate"])

class GenerateRequest(BaseModel):
    action_ids: List[str]
    formats: List[str] = ["claude"]  # claude, cursor, agents
    source: str = "scratch"  # "repo", "template", or "scratch"
    repo_url: Optional[str] = None  # For tracking the source repo when source="repo"

class GenerateResponse(BaseModel):
    files: Dict[str, str]
    patch: str
    source: str

@router.post("/generate", operation_id="generate_configuration")
async def generate_configuration(request: GenerateRequest) -> GenerateResponse:
    """Generate configuration files from selected action IDs"""
    
    files = {}
    
    # Load action details
    selected_agents = []
    selected_rules = []
    selected_mcps = []
    
    for action_id in request.action_ids:
        # Try to find the action in different categories
        
        # Check agents
        agent = actions_loader.get_agent(action_id)
        if agent:
            selected_agents.append(agent)
            continue
            
        # Check rules
        rule = actions_loader.get_rule(action_id)
        if rule:
            selected_rules.append(rule)
            continue
            
        # Check MCPs
        mcp = actions_loader.get_mcp(action_id)
        if mcp:
            selected_mcps.append(mcp)
            continue
    
    # Generate files based on selected formats
    for format_type in request.formats:
        if format_type == "claude":
            # Generate CLAUDE.md if there are rules
            if selected_rules:
                claude_content = ""
                for rule in selected_rules:
                    if rule.get('content'):
                        claude_content += rule['content'].strip() + "\n\n"
                
                if claude_content:
                    files['CLAUDE.md'] = claude_content.strip()
            
            # Generate agent files for Claude format
            for agent in selected_agents:
                if agent.get('content'):
                    filename = agent.get('filename', f"{agent['name']}.md")
                    files[f".claude/agents/{filename}"] = agent['content']
        
        elif format_type == "cursor":
            # Generate .cursorrules file
            if selected_rules:
                cursor_content = ""
                for rule in selected_rules:
                    if rule.get('content'):
                        cursor_content += rule['content'].strip() + "\n\n"
                
                if cursor_content:
                    files['.cursorrules'] = cursor_content.strip()
        
        elif format_type == "agents":
            # Generate AGENTS.md file with rules (copy of CLAUDE.md)
            if selected_rules:
                agents_content = ""
                for rule in selected_rules:
                    if rule.get('content'):
                        agents_content += rule['content'].strip() + "\n\n"
                
                if agents_content:
                    files['AGENTS.md'] = agents_content.strip()
    
    # Generate .mcp.json if there are MCPs
    if selected_mcps:
        mcp_config = {"mcpServers": {}}
        for mcp in selected_mcps:
            if mcp.get('config'):
                mcp_config["mcpServers"][mcp['name']] = mcp['config']
        
        if mcp_config["mcpServers"]:
            files['.mcp.json'] = json.dumps(mcp_config, indent=2)
    
    # Generate patch file
    patch = generate_patch(files, request.source, request.repo_url)
    
    return GenerateResponse(files=files, patch=patch, source=request.source)

def generate_patch(files: Dict[str, str], source: str = "scratch", repo_url: str = None) -> str:
    """
    Generate a unified diff patch from the files.
    
    Args:
        files: Dictionary of file paths and their contents
        source: Source of the generation ("repo", "template", or "scratch")
        repo_url: URL of source repository if source is "repo"
    
    Returns:
        Unified diff patch string that can be applied with patch command
    """
    patch_lines = []
    
    # Add a comment header explaining the patch
    if source == "repo" and repo_url:
        patch_lines.append(f"# Gitrules configuration patch generated from repository: {repo_url}")
        patch_lines.append("# Apply with: patch -p0 < <this-patch>")
    elif source == "template":
        patch_lines.append("# Gitrules configuration patch generated from template")
        patch_lines.append("# Apply with: patch -p0 < <this-patch>")
    else:
        patch_lines.append("# Gitrules configuration patch generated from scratch")
        patch_lines.append("# Apply with: patch -p0 < <this-patch>")
    
    patch_lines.append("")
    
    for filepath, content in files.items():
        # Standard patch format
        patch_lines.append(f"--- /dev/null")
        patch_lines.append(f"+++ {filepath}")
        
        lines = content.split('\n')
        if lines and lines[-1] == '':
            lines.pop()  # Remove empty last line if present
            
        patch_lines.append(f"@@ -0,0 +1,{len(lines)} @@")
        
        for line in lines:
            patch_lines.append(f"+{line}")
        
        patch_lines.append("")  # Empty line between files
    
    return '\n'.join(patch_lines)