from fastapi import APIRouter, HTTPException, Query
from app.models.actions import Action, ActionType, ActionsListResponse
from app.services.actions_loader import actions_loader
from typing import Optional

router = APIRouter(prefix="/api", tags=["actions"])

@router.get("/actions", response_model=ActionsListResponse, operation_id="get_unified_actions")
async def get_unified_actions(
    action_type: Optional[ActionType] = Query(None, description="Filter by action type"),
    tags: Optional[str] = Query(None, description="Comma-separated list of tags to filter by"),
    limit: int = Query(30, ge=1, le=100, description="Maximum number of results"),
    offset: int = Query(0, ge=0, description="Number of items to skip")
):
    """Get all actions in unified format with optional filtering"""
    # Parse tags if provided
    tag_list = None
    if tags:
        tag_list = [tag.strip() for tag in tags.split(',') if tag.strip()]
    
    # Get filtered actions
    filtered_actions = actions_loader.get_actions(
        action_type=action_type,
        tags=tag_list,
        limit=limit,
        offset=offset
    )
    
    # Get total count for pagination
    all_filtered = actions_loader.get_actions(
        action_type=action_type,
        tags=tag_list,
        limit=10000,  # Large number to get all
        offset=0
    )
    total = len(all_filtered)
    
    return ActionsListResponse(
        actions=filtered_actions,
        total=total,
        has_more=(offset + limit) < total
    )





