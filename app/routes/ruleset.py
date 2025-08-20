from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import PlainTextResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import hashlib
from typing import Dict
from datetime import datetime

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# In-memory storage for rulesets
rulesets_store: Dict[str, str] = {}

class RulesetCreate(BaseModel):
    files: Dict[str, str]

@router.post("/api/ruleset")
async def create_ruleset(request: Request, ruleset: RulesetCreate):
    """Generate install script from files and store by hash"""
    # Extract unique directories
    directories = set()
    for path in ruleset.files.keys():
        parts = path.split('/')
        if len(parts) > 1:
            for i in range(1, len(parts)):
                directories.add('/'.join(parts[:i]))
    
    # Generate script using Jinja2 template
    script_content = templates.get_template("install.sh.j2").render(
        timestamp=datetime.now().isoformat(),
        files=ruleset.files,
        directories=sorted(directories)
    )
    
    # Hash the script content
    content_hash = hashlib.sha256(script_content.encode()).hexdigest()[:12]
    rulesets_store[content_hash] = script_content
    
    return {"hash": content_hash}

@router.get("/api/ruleset/{hash_id}.sh", response_class=PlainTextResponse)
async def get_ruleset(hash_id: str):
    """Retrieve ruleset by hash"""
    if hash_id not in rulesets_store:
        raise HTTPException(status_code=404, detail="Ruleset not found")
    return rulesets_store[hash_id]