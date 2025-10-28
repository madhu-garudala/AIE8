# Enterprise Knowledge Management RAG System

A comprehensive Retrieval Augmented Generation (RAG) system designed specifically for enterprise knowledge management, supporting multiple document types, metadata filtering, and specialized use cases.

## 🚀 Features

### Core Capabilities
- **Multi-format Document Support**: PDF, DOCX, HTML, TXT, MD files
- **Metadata Management**: Department and category-based organization
- **Semantic Search**: Advanced vector-based document retrieval
- **Source Attribution**: Track document sources and relevance scores
- **Async Processing**: Efficient document processing and embedding generation

### Enterprise Features
- **Department Filtering**: Search within specific departments (HR, IT, Legal, etc.)
- **Category Filtering**: Filter by document types (policies, manuals, FAQs, etc.)
- **Specialized Use Cases**: Tailored prompts for different business functions
- **Metadata Inference**: Automatic department and category detection
- **Scalable Architecture**: Built for enterprise-scale knowledge bases

## 🏗️ Architecture

```
Enterprise RAG System
├── Document Processing
│   ├── EnterpriseDocumentLoader (Multi-format support)
│   ├── DocumentMetadata (Rich metadata management)
│   └── CharacterTextSplitter (Intelligent chunking)
├── Vector Database
│   ├── VectorDatabase (Enhanced with metadata)
│   ├── EmbeddingModel (OpenAI text-embedding-3-small)
│   └── Cosine Similarity Search
├── RAG Pipeline
│   ├── EnterpriseRAGPipeline (Specialized prompts)
│   ├── Use Case Templates (HR, IT, Legal, etc.)
│   └── Response Generation (GPT-4.1-mini)
└── Knowledge Manager
    ├── EnterpriseKnowledgeManager (High-level interface)
    ├── Statistics & Analytics
    └── Interactive Query Interface
```

## 📦 Installation

### Prerequisites
- Python 3.11+
- OpenAI API key

### Setup
1. Clone the repository
2. Install dependencies:
   ```bash
   uv sync
   ```
3. Set up your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

### Dependencies
- `openai>=1.59.7` - OpenAI API client
- `numpy>=1.24.0` - Numerical operations
- `PyPDF2>=3.0.0` - PDF text extraction
- `python-docx>=0.8.11` - DOCX text extraction
- `beautifulsoup4>=4.12.0` - HTML text extraction
- `nest-asyncio>=1.5.0` - Async support in Jupyter

## 🚀 Quick Start

### Basic Usage

```python
import asyncio
from aimakerspace.enterprise_rag import EnterpriseKnowledgeManager

async def main():
    # Initialize knowledge manager
    km = EnterpriseKnowledgeManager("path/to/your/documents/")
    await km.initialize()
    
    # Ask questions
    result = km.ask_question("What is our remote work policy?")
    print(result['response'])
    
    # Search with filters
    results = km.search_knowledge("benefits", department="hr")
    for result in results:
        print(f"{result['content']} (Score: {result['similarity_score']:.3f})")

asyncio.run(main())
```

### Interactive Demo

```bash
python enterprise_demo.py
```

## 📁 Document Organization

### Recommended Structure
```
enterprise_documents/
├── hr/
│   ├── policies/
│   │   ├── remote_work_policy.pdf
│   │   └── vacation_policy.docx
│   ├── procedures/
│   │   └── hiring_process.md
│   └── training/
│       └── onboarding_guide.html
├── it/
│   ├── manuals/
│   │   └── system_admin_guide.pdf
│   └── troubleshooting/
│       └── common_issues.md
├── legal/
│   ├── compliance/
│   │   └── gdpr_requirements.pdf
│   └── contracts/
│       └── standard_agreement.docx
└── marketing/
    ├── guides/
    │   └── brand_guidelines.pdf
    └── procedures/
        └── social_media_policy.md
```

### Automatic Metadata Detection
The system automatically infers:
- **Department**: Based on folder names (hr, it, legal, finance, marketing)
- **Category**: Based on file names (policy, manual, faq, training, procedure)

## 🎯 Use Cases

### 1. Company Wiki Assistant
```python
# General knowledge queries
result = km.ask_question("What is our company culture like?")
```

### 2. HR Support Bot
```python
# HR-specific queries with specialized prompts
result = km.ask_question(
    "How do I request time off?", 
    use_case="hr"
)
```

### 3. IT Help Desk
```python
# Technical support with IT-focused responses
result = km.ask_question(
    "How do I reset my password?", 
    use_case="it"
)
```

### 4. Legal Compliance
```python
# Legal and compliance queries
result = km.ask_question(
    "What are our data protection requirements?", 
    use_case="legal"
)
```

### 5. Customer Support
```python
# Customer-facing support
result = km.ask_question(
    "What are your product features?", 
    use_case="customer_support"
)
```

## 🔍 Advanced Search

### Department Filtering
```python
# Search only in HR documents
results = km.search_knowledge("benefits", department="hr")
```

### Category Filtering
```python
# Search only in policy documents
results = km.search_knowledge("remote work", category="policy")
```

### Combined Filtering
```python
# Search in IT manuals only
results = km.search_knowledge(
    "troubleshooting", 
    department="it", 
    category="manual"
)
```

## 📊 Analytics and Monitoring

### Knowledge Base Statistics
```python
stats = km.get_knowledge_stats()
print(f"Total documents: {stats['total_documents']}")
print(f"Departments: {stats['departments']}")
print(f"Categories: {stats['categories']}")
```

### Response Quality Analysis
```python
result = km.ask_question("Your question here")
print(f"Response length: {len(result['response'])}")
print(f"Sources used: {len(result['context'])}")
print(f"Average relevance: {sum(s['similarity_score'] for s in result['sources']) / len(result['sources'])}")
```

## 🛠️ Customization

### Adding New Document Types
Extend the `EnterpriseDocumentLoader` class:

```python
def _extract_custom_format(self, file_path: str) -> str:
    # Add your custom text extraction logic
    pass
```

### Creating Custom Use Cases
Add new system prompts to the `EnterpriseRAGPipeline`:

```python
def _get_custom_use_case_prompt(self) -> str:
    return """Your custom system prompt here..."""
```

### Custom Metadata Inference
Modify the metadata inference methods:

```python
def _infer_department(self, file_path: str) -> str:
    # Add your custom department detection logic
    pass
```

## 🔧 Configuration

### Environment Variables
```bash
export OPENAI_API_KEY="your-api-key"
export OPENAI_MODEL="gpt-4.1-mini"  # Optional
export EMBEDDING_MODEL="text-embedding-3-small"  # Optional
```

### Chunking Configuration
```python
splitter = CharacterTextSplitter(
    chunk_size=1000,      # Characters per chunk
    chunk_overlap=200     # Overlap between chunks
)
```

## 📈 Performance Optimization

### Async Processing
The system uses async processing for:
- Document loading
- Embedding generation
- Vector database building

### Batch Processing
Embeddings are processed in batches for efficiency:
```python
# Default batch size: 1024
embedding_model = EmbeddingModel(batch_size=1024)
```

### Memory Management
- Documents are processed in chunks
- Vectors are stored efficiently
- Metadata is indexed for fast filtering

## 🚀 Deployment

### Local Development
```bash
# Run the demo
python enterprise_demo.py

# Run Jupyter notebook
jupyter notebook Enterprise_RAG_Demo.ipynb
```

### Production Deployment
1. **Web Interface**: Create a Flask/FastAPI web app
2. **Database**: Use a proper vector database (Pinecone, Weaviate)
3. **Caching**: Implement Redis for response caching
4. **Monitoring**: Add logging and analytics
5. **Security**: Implement authentication and authorization

### Docker Deployment
```dockerfile
FROM python:3.11-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "enterprise_demo.py"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenAI for the embedding and language models
- AI Makerspace for the original RAG implementation
- The open-source community for the various libraries used

## 📞 Support

For questions and support:
- Create an issue on GitHub
- Contact the development team
- Check the documentation

---

**Built with ❤️ for enterprise knowledge management**
