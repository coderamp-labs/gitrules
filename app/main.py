from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.routes import install, actions, recommend, generate
from app.services.actions_loader import actions_loader
from api_analytics.fastapi import Analytics
from fastapi_mcp import FastApiMCP
import os
from dotenv import load_dotenv
from loguru import logger
import sys

# Load environment variables
load_dotenv()

# Configure loguru logger
logger.remove()
logger.add(
    sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO"
)
logger.add(
    "logs/app.log",
    rotation="10 MB",
    retention="7 days",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} - {message}",
    level="DEBUG"
)

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
app.include_router(recommend.router)
app.include_router(generate.router)

@app.get("/favicon.ico", operation_id="get_favicon")
async def favicon():
    favicon_path = static_dir / "favicon.ico"
    return FileResponse(favicon_path, media_type="image/x-icon")

@app.get("/doc", response_class=HTMLResponse, operation_id="get_docs_page")
async def doc(request: Request):
    return templates.TemplateResponse("docs.html", {"request": request})

@app.get("/select", response_class=HTMLResponse, operation_id="get_select_page")
async def select(request: Request):
    """Action selection page with filters"""
    return templates.TemplateResponse("select.html", {"request": request})

@app.get("/generate", response_class=HTMLResponse, operation_id="get_generate_page")
async def get_generate_page(request: Request):
    """Generate configuration files from selected actions"""
    return templates.TemplateResponse("generate.html", {"request": request})

@app.get("/", response_class=HTMLResponse, operation_id="get_index_page")
async def index(request: Request):
    """Landing page for starting the configuration journey"""
    return templates.TemplateResponse("landing.html", {"request": request})


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