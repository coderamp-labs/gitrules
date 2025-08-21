from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import PlainTextResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import hashlib
import re
from typing import Dict, Set
from datetime import datetime

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# In-memory storage for installs
installs_store: Dict[str, str] = {}

class InstallCreate(BaseModel):
    files: Dict[str, str]

def extract_env_vars_from_files(files: Dict[str, str]) -> Set[str]:
    """Extract environment variables from file contents"""
    env_vars = set()
    for content in files.values():
        # Find ${VAR_NAME} patterns
        matches = re.findall(r'\$\{([^}]+)\}', content)
        env_vars.update(matches)
    return env_vars

@router.post("/api/install")
async def create_install(request: Request, install: InstallCreate):
    """Generate install script from files and store by hash"""
    # Extract unique directories
    directories = set()
    for path in install.files.keys():
        parts = path.split('/')
        if len(parts) > 1:
            for i in range(1, len(parts)):
                directories.add('/'.join(parts[:i]))
    
    # Extract environment variables from all files
    env_vars = extract_env_vars_from_files(install.files)
    
    # Generate script using Jinja2 template
    script_content = templates.get_template("install.sh.j2").render(
        timestamp=datetime.now().isoformat(),
        files=install.files,
        directories=sorted(directories),
        env_vars=sorted(env_vars) if env_vars else None
    )
    
    # Hash the script content
    content_hash = hashlib.sha256(script_content.encode()).hexdigest()[:12]
    installs_store[content_hash] = script_content
    
    return {"hash": content_hash}

@router.get("/api/install/{hash_id}.sh", response_class=PlainTextResponse)
async def get_install(hash_id: str):
    """Retrieve install by hash"""
    if hash_id not in installs_store:
        raise HTTPException(status_code=404, detail="Install not found")
    return installs_store[hash_id]