"""Toolbelt assembly for agents.

Collects third-party tools and local tools (like RAG) into a single list that
graphs can bind to their language models.
"""
from __future__ import annotations

import os
from typing import List

from app.rag import retrieve_information


def get_tool_belt() -> List:
    """Return the list of tools available to agents (Tavily, Arxiv, RAG)."""
    tools = []
    
    # Only add Tavily if API key is available
    if os.environ.get("TAVILY_API_KEY"):
        from langchain_community.tools.tavily_search import TavilySearchResults
        tools.append(TavilySearchResults(max_results=5))
    
    # Add Arxiv tool (doesn't require API key)
    from langchain_community.tools.arxiv.tool import ArxivQueryRun
    tools.append(ArxivQueryRun())
    
    # Add RAG tool
    tools.append(retrieve_information)
    
    return tools


