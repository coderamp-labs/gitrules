from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.routes import install, actions, smart_ingest_route, recommend
from app.services.actions_loader import actions_loader
from api_analytics.fastapi import Analytics
from fastapi_mcp import FastApiMCP
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="Gitrules", version="0.1.0")

# Add API Analytics middleware
api_key = os.getenv("API_ANALYTICS_KEY")
if api_key:
    app.add_middleware(Analytics, api_key=api_key)

templates = Jinja2Templates(directory="app/templates")

static_dir = Path(__file__).parent / "static"
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Include routers
app.include_router(install.router)
app.include_router(actions.router)
app.include_router(smart_ingest_route.router)
app.include_router(recommend.router)

@app.get("/favicon.ico", operation_id="get_favicon")
async def favicon():
    favicon_path = static_dir / "favicon.ico"
    return FileResponse(favicon_path, media_type="image/x-icon")

@app.get("/doc", response_class=HTMLResponse, operation_id="get_docs_page")
async def doc(request: Request):
    return templates.TemplateResponse("docs.html", {"request": request})

@app.get("/", response_class=HTMLResponse, operation_id="get_index_page")
async def index(request: Request):
    # Get all actions data for server-side rendering
    agents = [agent.dict() for agent in actions_loader.get_agents()]
    all_rules = actions_loader.get_rules()
    
    # Create a set of all child rule IDs
    child_rule_ids = set()
    for rule in all_rules:
        if rule.children:
            child_rule_ids.update(rule.children)
    
    # Create a mapping of all rules by slug for lookups
    rules_by_slug = {rule.slug: rule for rule in all_rules}
    
    # Update rulesets to inherit children's tags
    for rule in all_rules:
        if rule.type == 'ruleset' and rule.children:
            # Collect all tags from children
            inherited_tags = set(rule.tags or [])
            for child_slug in rule.children:
                child_rule = rules_by_slug.get(child_slug)
                if child_rule and child_rule.tags:
                    inherited_tags.update(child_rule.tags)
            rule.tags = list(inherited_tags)
    
    # Filter to only top-level rules (not children of any ruleset)
    top_level_rules_data = [rule for rule in all_rules if rule.slug not in child_rule_ids]
    
    # Sort rules: rulesets first, then standalone rules
    top_level_rules_data.sort(key=lambda rule: (rule.type != 'ruleset', rule.display_name or rule.name))
    
    # Convert to dict
    top_level_rules = [rule.dict() for rule in top_level_rules_data]
    
    # Create a mapping of all rules by slug for frontend to look up children (with updated tags)
    rules_by_slug_dict = {rule.slug: rule.dict() for rule in all_rules}
    
    mcps = [mcp.dict() for mcp in actions_loader.get_mcps()]
    
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "agents": agents,
            "rules": top_level_rules,
            "rules_by_slug": rules_by_slug_dict,
            "mcps": mcps
        }
    )

@app.get("/health", operation_id="health_check")
async def health_check():
    return {"status": "healthy"}

# Create MCP server that only exposes endpoints tagged with "mcp"
mcp = FastApiMCP(
    app,
    name="gitrules-search",
    include_tags=["mcp"]
)

# Mount the MCP server with HTTP/SSE transport
mcp.mount_http(mount_path="/mcp")