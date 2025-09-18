#!/usr/bin/env python3
"""
Test script for enterprise search RAG system
"""

import asyncio
import os
from getpass import getpass
from aimakerspace.enterprise_rag import EnterpriseKnowledgeManager


async def test_enterprise_search():
    """Test the RAG system with enterprise data."""
    print("🏢 Testing Enterprise Search RAG System")
    print("=" * 50)
    
    # Set up OpenAI API key
    openai_api_key = getpass("Enter your OpenAI API key: ")
    os.environ["OPENAI_API_KEY"] = openai_api_key
    print("✅ OpenAI API key configured!")
    
    # Initialize knowledge manager
    print("\n📚 Initializing knowledge base...")
    km = EnterpriseKnowledgeManager("data/")
    await km.initialize()
    
    # Show knowledge base stats
    stats = km.get_knowledge_stats()
    print(f"\n📊 Knowledge Base Statistics:")
    print(f"   Documents: {stats['total_documents']}")
    print(f"   Departments: {', '.join(stats['departments'])}")
    print(f"   Categories: {', '.join(stats['categories'])}")
    
    # Test queries about enterprise data
    test_queries = [
        "Where is the headquarters located?",
        "Who is the CEO?",
        "What are the office locations?",
        "Who is the CFO?",
        "Where is the Princeton office?",
        "Who is the CTO?",
        "What is the Arlington office address?"
    ]
    
    print(f"\n🎯 Testing {len(test_queries)} queries about enterprise data...")
    print("=" * 50)
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n{i}. Question: {query}")
        
        try:
            result = km.ask_question(query)
            print(f"   Answer: {result['response']}")
            print(f"   Sources: {len(result['context'])} documents found")
            
            if result['sources']:
                for j, source in enumerate(result['sources'][:2], 1):
                    print(f"   Source {j}: {source['filename']} (Score: {source['similarity_score']:.3f})")
                    print(f"              Department: {source['department']}, Category: {source['category']}")
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print(f"\n✅ Test completed!")


if __name__ == "__main__":
    asyncio.run(test_enterprise_search())
