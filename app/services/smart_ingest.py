"""
Functions for ingesting repositories and sending context to OpenAI API.
"""

import httpx
from typing import Optional, Dict, Any
from dotenv import load_dotenv
import os
from loguru import logger

# Load environment variables from .env file
load_dotenv()


async def use_gitingest(url: str, context_size: int = 50000) -> str:
    """
    Ingest a repository using gitingest.com API and trim to specified token size.
    
    Args:
        url: Repository URL to ingest
        context_size: Maximum context size in tokens (default ~50k tokens)
    
    Returns:
        String containing the repository context, trimmed to specified size
    """
    logger.info(f"Ingesting repository from {url}")
    # Query gitingest.com API instead of local package
    async with httpx.AsyncClient(timeout=120.0) as client:
        try:
            # Call gitingest.com API
            response = await client.post(
                "https://gitingest.com/api/ingest",
                json={
                    "input_text": url,
                    "max_file_size": 102400,
                    "pattern_type": "exclude",
                    "pattern": "",
                    "token": ""
                },
                headers={
                    "Content-Type": "application/json"
                }
            )
            response.raise_for_status()
            
            # Parse response - assuming it returns the full context
            data = response.json()
            full_context = data.get("content", "")
            
            # If the API returns structured data, combine it
            if isinstance(data, dict) and "summary" in data:
                summary = data.get("summary", "")
                tree = data.get("tree", "")
                content = data.get("content", "")
                full_context = f"{summary}\n\n{tree}\n\n{content}"
            
        except httpx.HTTPError as e:
            logger.error(f"Failed to ingest repository from gitingest.com: {str(e)}")
            raise Exception(f"Failed to ingest repository from gitingest.com: {str(e)}")
    
    # Approximate token count (roughly 4 chars per token)
    # Trim to specified context size
    max_chars = context_size * 4
    original_length = len(full_context)
    if len(full_context) > max_chars:
        full_context = full_context[:max_chars]
        # Add ellipsis to indicate truncation
        full_context += "\n\n... (context truncated)"
        logger.info(f"Context truncated from {original_length} to {len(full_context)} characters")
    else:
        logger.info(f"Repository context ingested: {len(full_context)} characters")
    
    return full_context


def smart_ingest(
    context: str, 
    user_prompt: str = "Analyze this repository and provide insights",
    api_key: Optional[str] = None
) -> Dict[str, Any]:
    """
    Send the ingested repository context to OpenAI API with a system prompt.
    
    Args:
        context: The "big fat context" from use_git_ingest function
        user_prompt: The user's question or request about the repository
        api_key: Optional OpenAI API key (defaults to env var OPENAI_API_KEY)
    
    Returns:
        Dictionary containing OpenAI's response and metadata
    
    Raises:
        Exception: If the API call fails
    """
    # Get API key from environment if not provided
    if not api_key:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
    
    # System prompt for repository analysis
    system_prompt = """You are an expert code analyst and software architect. 
You have been given the complete context of a repository including its structure and file contents.
Analyze the repository thoroughly and provide insights based on the user's request.
Focus on:
- Code quality and architecture
- Potential improvements
- Security considerations
- Documentation completeness
- Dependencies and technical debt
Be specific and provide actionable recommendations."""
    
    # Prepare messages for OpenAI
    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": f"{user_prompt}\n\n{context}"
        }
    ]
    
    # OpenAI API endpoint
    url = "https://api.openai.com/v1/chat/completions"
    
    # Headers for the API request
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Request body
    data = {
        "model": "gpt-4o-mini",  # Using GPT-4o-mini for cost efficiency
        "messages": messages,
        "temperature": 0.3,  # Lower temperature for more focused analysis
        "max_tokens": 4096
    }
    
    try:
        # Make the API call
        with httpx.Client(timeout=60.0) as client:
            response = client.post(url, json=data, headers=headers)
            response.raise_for_status()
            
            result = response.json()
            
            # Extract the response
            choice = result.get("choices", [{}])[0]
            message = choice.get("message", {})
            
            return {
                "success": True,
                "response": message.get("content", ""),
                "model": result.get("model"),
                "usage": result.get("usage", {}),
                "finish_reason": choice.get("finish_reason")
            }
            
    except httpx.HTTPStatusError as e:
        error_detail = e.response.text if e.response else str(e)
        logger.error(f"OpenAI API error: {e.response.status_code} - {error_detail}")
        raise Exception(f"OpenAI API error: {e.response.status_code} - {error_detail}")
    except Exception as e:
        logger.error(f"Failed to send context to OpenAI: {str(e)}")
        raise Exception(f"Failed to send context to OpenAI: {str(e)}")