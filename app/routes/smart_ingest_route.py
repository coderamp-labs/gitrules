"""
Simple route for smart ingest functionality.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.services.smart_ingest import use_gitingest, smart_ingest

router = APIRouter(prefix="/api", tags=["smart_ingest"])


class IngestRequest(BaseModel):
    repo_url: str


class IngestResponse(BaseModel):
    success: bool
    context_size: int
    message: str


class AnalyzeRequest(BaseModel):
    context: str
    user_prompt: Optional[str] = "Analyze this repository and provide a comprehensive overview"


class AnalyzeResponse(BaseModel):
    success: bool
    analysis: str


@router.post("/ingest", response_model=IngestResponse)
async def ingest_repository(request: IngestRequest):
    """
    Ingest a repository and return the context.
    """
    try:
        context = await use_gitingest(request.repo_url)
        return IngestResponse(
            success=True,
            context_size=len(context),
            message=context
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_context(request: AnalyzeRequest):
    """
    Analyze the provided context using OpenAI.
    """
    try:
        result = smart_ingest(request.context, request.user_prompt)
        return AnalyzeResponse(
            success=True,
            analysis=result.get("response", "")
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Keep the combined endpoint for backward compatibility
class SmartIngestRequest(BaseModel):
    repo_url: str
    user_prompt: Optional[str] = "Analyze this repository and provide a comprehensive overview"


class SmartIngestResponse(BaseModel):
    success: bool
    analysis: str


@router.post("/smart_ingest", response_model=SmartIngestResponse)
async def analyze_repository(request: SmartIngestRequest):
    """
    Analyze a repository using smart ingest (combined endpoint).
    """
    try:
        # Step 1: Ingest the repository (async)
        context = await use_gitingest(request.repo_url)
        
        # Step 2: Send to OpenAI (still sync, but that's ok)
        result = smart_ingest(context, request.user_prompt)
        
        return SmartIngestResponse(
            success=True,
            analysis=result.get("response", "")
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))