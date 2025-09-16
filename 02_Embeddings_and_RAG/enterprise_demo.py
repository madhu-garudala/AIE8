#!/usr/bin/env python3
"""
Enterprise RAG Demo Script
Demonstrates the enterprise knowledge management RAG system.
"""

import asyncio
import os
from getpass import getpass
from aimakerspace.enterprise_rag import EnterpriseKnowledgeManager


async def main():
    """Main demo function."""
    print("🏢 Enterprise Knowledge Management RAG System")
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
    print(f"   Use Cases: {', '.join(stats['use_cases'])}")
    
    # Demo queries
    demo_queries = [
        {
            "question": "What is the Michael Eisner Memorial Weak Executive Problem?",
            "use_case": "general",
            "description": "General business knowledge"
        },
        {
            "question": "What should I know about hiring executives?",
            "use_case": "hr",
            "description": "HR-specific guidance"
        },
        {
            "question": "How do I approach startup funding decisions?",
            "use_case": "general",
            "description": "Entrepreneurship guidance"
        }
    ]
    
    print(f"\n🎯 Running {len(demo_queries)} demo queries...")
    print("=" * 50)
    
    for i, demo in enumerate(demo_queries, 1):
        print(f"\n{i}. {demo['description']}")
        print(f"   Question: {demo['question']}")
        
        try:
            result = km.ask_question(
                demo['question'],
                use_case=demo['use_case']
            )
            
            print(f"   Answer: {result['response'][:200]}...")
            print(f"   Sources: {len(result['context'])} documents")
            
            if result['sources']:
                avg_score = sum(s['similarity_score'] for s in result['sources']) / len(result['sources'])
                print(f"   Avg Relevance: {avg_score:.3f}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    # Interactive mode
    print(f"\n🤖 Interactive Mode (type 'quit' to exit)")
    print("-" * 30)
    
    while True:
        try:
            query = input("\nAsk a question: ").strip()
            
            if query.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if query.lower() == 'help':
                print("\nAvailable commands:")
                print("- Ask any question about the knowledge base")
                print("- 'stats' - Show knowledge base statistics")
                print("- 'departments' - List available departments")
                print("- 'categories' - List available categories")
                print("- 'quit' - Exit the program")
                continue
            
            if query.lower() == 'stats':
                stats = km.get_knowledge_stats()
                print(f"\n📊 Knowledge Base: {stats['total_documents']} documents")
                print(f"🏢 Departments: {', '.join(stats['departments'])}")
                print(f"📂 Categories: {', '.join(stats['categories'])}")
                continue
            
            if query.lower() == 'departments':
                departments = km.rag_pipeline.get_available_departments()
                print(f"\n🏢 Available departments: {', '.join(departments)}")
                continue
            
            if query.lower() == 'categories':
                categories = km.rag_pipeline.get_available_categories()
                print(f"\n📂 Available categories: {', '.join(categories)}")
                continue
            
            if query:
                result = km.ask_question(query)
                print(f"\n💡 Answer: {result['response']}")
                print(f"📚 Sources: {len(result['context'])} documents found")
                
                if result['sources']:
                    print("\n📋 Source Details:")
                    for i, source in enumerate(result['sources'][:3], 1):
                        print(f"   {i}. {source['filename']} (Score: {source['similarity_score']:.3f})")
                        print(f"      Department: {source['department']}, Category: {source['category']}")
        
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
