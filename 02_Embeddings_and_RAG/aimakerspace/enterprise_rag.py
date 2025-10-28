"""
Enterprise RAG Pipeline for Knowledge Management
Supports multiple document types, metadata filtering, and specialized use cases.
"""

from typing import List, Dict, Any, Optional, Tuple
from aimakerspace.vectordatabase import VectorDatabase
from aimakerspace.openai_utils.chatmodel import ChatOpenAI
from aimakerspace.openai_utils.prompts import SystemRolePrompt, UserRolePrompt
from aimakerspace.text_utils import EnterpriseDocumentLoader, DocumentMetadata
import asyncio


class EnterpriseRAGPipeline:
    """Enhanced RAG pipeline for enterprise knowledge management."""
    
    def __init__(self, 
                 llm: ChatOpenAI, 
                 vector_db: VectorDatabase,
                 response_style: str = "professional",
                 include_sources: bool = True):
        self.llm = llm
        self.vector_db = vector_db
        self.response_style = response_style
        self.include_sources = include_sources
        
        # Enterprise-specific prompts
        self.system_prompts = {
            "general": self._get_general_system_prompt(),
            "hr": self._get_hr_system_prompt(),
            "it": self._get_it_system_prompt(),
            "legal": self._get_legal_system_prompt(),
            "compliance": self._get_compliance_system_prompt(),
            "customer_support": self._get_customer_support_prompt()
        }
    
    def _get_general_system_prompt(self) -> str:
        return """You are an intelligent enterprise knowledge assistant. You help employees find information from company documents and provide accurate, helpful responses.

Instructions:
- Answer questions using only information from the provided context
- If the context doesn't contain relevant information, respond with "I don't have information about that in our knowledge base"
- Be professional, clear, and concise
- When citing sources, mention the document type and department
- If you're unsure about something, say so rather than guessing
- Keep responses {response_style} and {response_length}"""

    def _get_hr_system_prompt(self) -> str:
        return """You are an HR knowledge assistant specializing in human resources policies, procedures, and employee information.

Instructions:
- Provide accurate information about HR policies, benefits, procedures, and employee guidelines
- Always reference specific policy documents when available
- Be sensitive to confidential information - only share what's appropriate
- If discussing sensitive topics, recommend speaking with HR directly
- Keep responses professional and supportive
- When in doubt, suggest contacting HR for clarification"""

    def _get_it_system_prompt(self) -> str:
        return """You are an IT support assistant helping with technical documentation, procedures, and troubleshooting.

Instructions:
- Provide clear, step-by-step technical guidance
- Reference specific documentation and procedures
- Include relevant error codes, system names, and technical details
- Suggest escalation paths for complex issues
- Be precise with technical terminology
- Include relevant links or references when available"""

    def _get_legal_system_prompt(self) -> str:
        return """You are a legal knowledge assistant providing information about company policies, compliance requirements, and legal procedures.

Instructions:
- Provide accurate information about legal policies and compliance requirements
- Always reference specific legal documents and policy numbers
- Emphasize the importance of consulting with legal counsel for complex matters
- Be precise with legal terminology and requirements
- Include relevant deadlines, requirements, and procedures
- When discussing sensitive legal matters, recommend legal consultation"""

    def _get_compliance_system_prompt(self) -> str:
        return """You are a compliance assistant helping ensure adherence to company policies and regulatory requirements.

Instructions:
- Provide accurate information about compliance requirements and procedures
- Reference specific policy documents and regulatory guidelines
- Emphasize the importance of following proper procedures
- Include relevant deadlines, requirements, and reporting obligations
- Be clear about consequences of non-compliance
- When in doubt, recommend consulting with compliance officers"""

    def _get_customer_support_prompt(self) -> str:
        return """You are a customer support assistant helping with product information, FAQs, and customer inquiries.

Instructions:
- Provide helpful, accurate information about products and services
- Reference specific documentation, FAQs, and product guides
- Be friendly and professional in your responses
- Include relevant product details, features, and specifications
- Suggest appropriate escalation paths for complex issues
- Always prioritize customer satisfaction and clear communication"""

    def run_pipeline(self, 
                    user_query: str, 
                    k: int = 4,
                    department: Optional[str] = None,
                    category: Optional[str] = None,
                    use_case: str = "general",
                    response_length: str = "detailed") -> Dict[str, Any]:
        """Run the enterprise RAG pipeline with enhanced filtering and use case specialization."""
        
        # Search with metadata filtering
        if department or category:
            context_list = self.vector_db.search_with_metadata(
                user_query, k=k, 
                department_filter=department, 
                category_filter=category
            )
        else:
            context_list = self.vector_db.search_with_metadata(user_query, k=k)
        
        # Build context with metadata information
        context_prompt = ""
        sources_info = []
        
        for i, (context, score, metadata) in enumerate(context_list, 1):
            context_prompt += f"[Source {i}]: {context}\n\n"
            
            if metadata:
                source_info = {
                    "source_id": i,
                    "filename": metadata.filename,
                    "department": metadata.department,
                    "category": metadata.category,
                    "file_type": metadata.file_type,
                    "similarity_score": score
                }
                sources_info.append(source_info)
        
        # Get appropriate system prompt
        system_prompt_template = self.system_prompts.get(use_case, self.system_prompts["general"])
        system_prompt = SystemRolePrompt(system_prompt_template)
        
        # Create user prompt with enhanced context
        user_prompt_template = """Context Information:
{context}

Number of relevant sources found: {context_count}
Department filter: {department_filter}
Category filter: {category_filter}
Use case: {use_case}

Question: {user_query}

Please provide your answer based solely on the context above."""

        user_prompt = UserRolePrompt(user_prompt_template)
        
        # Format prompts
        system_message = system_prompt.create_message(
            response_style=self.response_style,
            response_length=response_length
        )
        
        user_message = user_prompt.create_message(
            user_query=user_query,
            context=context_prompt.strip(),
            context_count=len(context_list),
            department_filter=department or "All",
            category_filter=category or "All",
            use_case=use_case.title()
        )
        
        # Get LLM response
        response = self.llm.run([system_message, user_message])
        
        return {
            "response": response,
            "context": context_list,
            "sources": sources_info if self.include_sources else None,
            "metadata": {
                "department_filter": department,
                "category_filter": category,
                "use_case": use_case,
                "response_style": self.response_style,
                "response_length": response_length
            },
            "prompts_used": {
                "system": system_message,
                "user": user_message
            }
        }

    def get_available_departments(self) -> List[str]:
        """Get list of available departments in the knowledge base."""
        return self.vector_db.get_departments()

    def get_available_categories(self) -> List[str]:
        """Get list of available categories in the knowledge base."""
        return self.vector_db.get_categories()

    def get_use_cases(self) -> List[str]:
        """Get list of available use cases."""
        return list(self.system_prompts.keys())

    def search_documents(self, 
                        query: str, 
                        k: int = 5,
                        department: Optional[str] = None,
                        category: Optional[str] = None) -> List[Dict[str, Any]]:
        """Search documents and return detailed results with metadata."""
        results = self.vector_db.search_with_metadata(
            query, k=k, 
            department_filter=department, 
            category_filter=category
        )
        
        search_results = []
        for text, score, metadata in results:
            result = {
                "content": text[:200] + "..." if len(text) > 200 else text,
                "similarity_score": score,
                "metadata": metadata.to_dict() if metadata else None
            }
            search_results.append(result)
        
        return search_results


class EnterpriseKnowledgeManager:
    """High-level interface for enterprise knowledge management."""
    
    def __init__(self, knowledge_base_path: str):
        self.knowledge_base_path = knowledge_base_path
        self.vector_db = None
        self.rag_pipeline = None
        self.documents = []
        self.metadata = []
    
    async def initialize(self):
        """Initialize the knowledge base from documents."""
        print("Loading enterprise documents...")
        
        # Load documents with metadata
        loader = EnterpriseDocumentLoader(self.knowledge_base_path)
        self.documents, self.metadata = loader.load_documents()
        
        print(f"Loaded {len(self.documents)} documents")
        print(f"Departments found: {set(m.department for m in self.metadata)}")
        print(f"Categories found: {set(m.category for m in self.metadata)}")
        
        # Build vector database
        print("Building vector database...")
        self.vector_db = VectorDatabase()
        self.vector_db = await self.vector_db.abuild_from_enterprise_docs(
            self.documents, self.metadata
        )
        
        # Initialize RAG pipeline
        self.rag_pipeline = EnterpriseRAGPipeline(
            llm=ChatOpenAI(),
            vector_db=self.vector_db
        )
        
        print("Enterprise knowledge manager initialized successfully!")
    
    def ask_question(self, 
                    question: str,
                    department: Optional[str] = None,
                    category: Optional[str] = None,
                    use_case: str = "general") -> Dict[str, Any]:
        """Ask a question to the knowledge base."""
        if not self.rag_pipeline:
            raise ValueError("Knowledge manager not initialized. Call initialize() first.")
        
        return self.rag_pipeline.run_pipeline(
            user_query=question,
            department=department,
            category=category,
            use_case=use_case
        )
    
    def search_knowledge(self, 
                        query: str,
                        department: Optional[str] = None,
                        category: Optional[str] = None) -> List[Dict[str, Any]]:
        """Search the knowledge base for relevant documents."""
        if not self.rag_pipeline:
            raise ValueError("Knowledge manager not initialized. Call initialize() first.")
        
        return self.rag_pipeline.search_documents(
            query=query,
            department=department,
            category=category
        )
    
    def get_knowledge_stats(self) -> Dict[str, Any]:
        """Get statistics about the knowledge base."""
        if not self.vector_db:
            return {"error": "Knowledge base not initialized"}
        
        return {
            "total_documents": len(self.documents),
            "departments": self.vector_db.get_departments(),
            "categories": self.vector_db.get_categories(),
            "use_cases": self.rag_pipeline.get_use_cases() if self.rag_pipeline else []
        }


# Example usage and testing
if __name__ == "__main__":
    async def main():
        # Initialize knowledge manager
        km = EnterpriseKnowledgeManager("data/")
        await km.initialize()
        
        # Example queries
        print("\n=== Enterprise Knowledge Management Demo ===\n")
        
        # General question
        result = km.ask_question("What is the company policy on remote work?")
        print("Q: What is the company policy on remote work?")
        print(f"A: {result['response']}\n")
        
        # Department-specific question
        result = km.ask_question("How do I reset my password?", use_case="it")
        print("Q: How do I reset my password? (IT use case)")
        print(f"A: {result['response']}\n")
        
        # Search documents
        search_results = km.search_knowledge("benefits", category="policy")
        print("Search results for 'benefits' in policy category:")
        for i, result in enumerate(search_results[:3], 1):
            print(f"{i}. {result['content']} (Score: {result['similarity_score']:.3f})")
        
        # Knowledge base stats
        stats = km.get_knowledge_stats()
        print(f"\nKnowledge Base Stats: {stats}")
    
    # Run the demo
    asyncio.run(main())
