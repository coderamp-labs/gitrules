"""
Route for tool recommendations based on repository analysis.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, List
from app.services.smart_ingest import use_gitingest
from app.services.recommend_tools import (
    build_tools_catalog,
    get_catalog_version,
    format_catalog_for_prompt,
    call_llm_for_reco,
    parse_and_validate
)

router = APIRouter(prefix="/api", tags=["recommend"])


class RecommendRequest(BaseModel):
    repo_url: Optional[str] = None
    context: Optional[str] = None
    user_prompt: Optional[str] = "Pick minimal useful tools for this repo"


class PreselectionData(BaseModel):
    rules: List[str]
    agents: List[str]
    mcps: List[str]


class RecommendResponse(BaseModel):
    success: bool
    preselect: PreselectionData
    rationales: Optional[Dict[str, str]] = None
    context_size: int
    catalog_version: str
    raw: Optional[str] = None  # For debugging


@router.post("/recommend", response_model=RecommendResponse)
async def recommend_tools(request: RecommendRequest):
    """
    Analyze a repository and recommend minimal useful tools.
    
    Accepts either repo_url (for ingestion) or context (pre-ingested).
    Returns a minimal selection of rules, agents, and MCPs.
    """
    try:
        # Validate input - need at least one
        if not request.repo_url and not request.context:
            raise HTTPException(
                status_code=400,
                detail="Either repo_url or context must be provided"
            )
        print(f"Getting context for {request.repo_url}")
        # Step 1: Get context (ingest if needed)
        if request.context:
            print(f"Using provided context")
            context = request.context
        else:
            # Ingest the repository
            print(f"Ingesting repository {request.repo_url}")
            context = await use_gitingest(request.repo_url)
        context_size = len(context)
        print(f"Context size: {context_size}")
        
        # Step 2: Build catalog
        catalog = build_tools_catalog()
        catalog_version = get_catalog_version(catalog)
        
        # Step 3: Format catalog for LLM
        catalog_text = format_catalog_for_prompt(catalog)
        
        # Step 4: Call LLM
        llm_raw = call_llm_for_reco(
            context=context,
            catalog_text=catalog_text,
            user_prompt=request.user_prompt or ""
        )
        
        # Step 5: Parse and validate
        preselect, rationales = parse_and_validate(llm_raw, catalog)
        
        return RecommendResponse(
            success=True,
            preselect=PreselectionData(**preselect),
            rationales=rationales,
            context_size=context_size,
            catalog_version=catalog_version,
            raw=llm_raw  # Include for debugging
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))