from typing import List, Optional, Dict, Any
from fuzzywuzzy import fuzz
from app.models.actions import Agent, Rule, MCP
from app.services.actions_loader import actions_loader
import re
import fnmatch

class SearchService:
    def __init__(self):
        self.actions_loader = actions_loader
    
    def _is_wildcard_query(self, query: str) -> bool:
        """Check if query contains wildcard characters"""
        return '*' in query or '?' in query
    
    def _wildcard_match(self, pattern: str, text: str) -> bool:
        """Check if text matches wildcard pattern"""
        return fnmatch.fnmatch(text.lower(), pattern.lower())
    
    def _calculate_relevance(self, query: str, text: str) -> int:
        """Calculate relevance score for fuzzy matching with wildcard support"""
        if not text:
            return 0
        query_lower = query.lower()
        text_lower = text.lower()
        
        # Handle wildcard queries
        if self._is_wildcard_query(query):
            if self._wildcard_match(query, text):
                return 95  # High score for wildcard matches
            else:
                return 0
        
        # Exact match gets highest score
        if query_lower == text_lower:
            return 100
        
        # Substring match gets high score
        if query_lower in text_lower:
            return 90
        
        # Use fuzzy matching for partial matches
        return fuzz.partial_ratio(query_lower, text_lower)
    
    def search_agents(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search for agents by name, display_name, or content"""
        agents = self.actions_loader.get_agents()
        results = []
        
        for agent in agents:
            # Calculate relevance scores for different fields
            name_score = self._calculate_relevance(query, agent.name)
            display_score = self._calculate_relevance(query, agent.display_name or "")
            content_score = self._calculate_relevance(query, agent.content or "") * 0.5  # Lower weight for content
            
            max_score = max(name_score, display_score, content_score)
            
            if max_score > 30:  # Threshold for relevance
                agent_data = agent.dict()
                # Remove content from search results
                agent_data.pop("content", None)
                results.append({
                    "agent": agent_data,
                    "relevance": max_score
                })
        
        # Sort by relevance and limit results
        results.sort(key=lambda x: x["relevance"], reverse=True)
        return results[:limit]
    
    def search_rules(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search for rules by name, display_name, content, tags, or author"""
        rules = self.actions_loader.get_rules()
        results = []
        
        for rule in rules:
            # Calculate relevance scores for different fields
            name_score = self._calculate_relevance(query, rule.name)
            display_score = self._calculate_relevance(query, rule.display_name or "")
            content_score = self._calculate_relevance(query, rule.content or "") * 0.5
            author_score = self._calculate_relevance(query, rule.author or "") * 0.7
            
            # Check tags
            tag_score = 0
            if rule.tags:
                for tag in rule.tags:
                    tag_score = max(tag_score, self._calculate_relevance(query, tag))
            
            max_score = max(name_score, display_score, content_score, author_score, tag_score)
            
            if max_score > 30:  # Threshold for relevance
                rule_data = rule.dict()
                # Remove content from search results
                rule_data.pop("content", None)
                results.append({
                    "rule": rule_data,
                    "relevance": max_score
                })
        
        # Sort by relevance and limit results
        results.sort(key=lambda x: x["relevance"], reverse=True)
        return results[:limit]
    
    def search_mcps(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Search for MCPs by name or config content"""
        mcps = self.actions_loader.get_mcps()
        results = []
        
        for mcp in mcps:
            # Calculate relevance scores
            name_score = self._calculate_relevance(query, mcp.name)
            
            # Search in config (convert to string for searching)
            config_str = str(mcp.config)
            config_score = self._calculate_relevance(query, config_str) * 0.5
            
            max_score = max(name_score, config_score)
            
            if max_score > 30:  # Threshold for relevance
                mcp_data = mcp.dict()
                # Remove config from search results
                mcp_data.pop("config", None)
                results.append({
                    "mcp": mcp_data,
                    "relevance": max_score
                })
        
        # Sort by relevance and limit results
        results.sort(key=lambda x: x["relevance"], reverse=True)
        return results[:limit]
    
    def search_all(self, query: str, limit: int = 10) -> Dict[str, Any]:
        """Search across all types (agents, rules, MCPs)"""
        return {
            "agents": self.search_agents(query, limit),
            "rules": self.search_rules(query, limit),
            "mcps": self.search_mcps(query, limit)
        }

# Create singleton instance
search_service = SearchService()