from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.routes import install, actions
from api_analytics.fastapi import Analytics
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

@app.get("/favicon.ico")
async def favicon():
    favicon_path = static_dir / "favicon.ico"
    return FileResponse(favicon_path, media_type="image/x-icon")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.get("/health")
async def health_check():
    return {"status": "healthy"}