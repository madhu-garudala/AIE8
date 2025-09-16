#!/usr/bin/env python3
"""
Enterprise Search RAG Demo
A simple interactive demo for asking questions about enterprise data.
"""

import asyncio
import os
from aimakerspace.enterprise_rag import EnterpriseKnowledgeManager


async def main():
    """Main demo function."""
    print("🏢 Enterprise Search RAG System")
    print("=" * 40)
    
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Please set your OpenAI API key as an environment variable:")
        print("   export OPENAI_API_KEY='your-api-key-here'")
        print("\nThen run this script again.")
        return
    
    print("✅ OpenAI API key found!")
    
    # Initialize knowledge manager
    print("\n📚 Loading enterprise data...")
    km = EnterpriseKnowledgeManager("data/")
    await km.initialize()
    
    # Show what we loaded
    stats = km.get_knowledge_stats()
    print(f"✅ Loaded {stats['total_documents']} document(s)")
    
    # Interactive mode
    print(f"\n🤖 Ask questions about enterprise data (type 'quit' to exit)")
    print("-" * 50)
    
    while True:
        try:
            query = input("\n❓ Your question: ").strip()
            
            if query.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            if not query:
                continue
            
            if query.lower() == 'help':
                print("\n💡 Try asking:")
                print("   - Where is the headquarters located?")
                print("   - Who is the CEO?")
                print("   - What are the office locations?")
                print("   - Who is the CFO?")
                print("   - Where is the Princeton office?")
                continue
            
            # Ask the question
            result = km.ask_question(query)
            print(f"\n💡 Answer: {result['response']}")
            
            if result['sources']:
                print(f"📚 Source: {result['sources'][0]['filename']}")
        
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
