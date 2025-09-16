import os
from typing import List, Dict, Any, Optional
import mimetypes
from pathlib import Path


class DocumentMetadata:
    """Class to store document metadata for enterprise knowledge management."""
    def __init__(self, 
                 file_path: str, 
                 file_type: str, 
                 department: str = "general",
                 category: str = "document",
                 last_modified: Optional[str] = None,
                 author: Optional[str] = None,
                 tags: List[str] = None):
        self.file_path = file_path
        self.file_type = file_type
        self.department = department
        self.category = category
        self.last_modified = last_modified
        self.author = author
        self.tags = tags or []
        self.filename = Path(file_path).name

    def to_dict(self) -> Dict[str, Any]:
        return {
            "file_path": self.file_path,
            "file_type": self.file_type,
            "department": self.department,
            "category": self.category,
            "last_modified": self.last_modified,
            "author": self.author,
            "tags": self.tags,
            "filename": self.filename
        }


class EnterpriseDocumentLoader:
    """Enhanced document loader for enterprise knowledge management."""
    
    def __init__(self, path: str, encoding: str = "utf-8"):
        self.documents = []
        self.metadata = []
        self.path = path
        self.encoding = encoding
        self.supported_extensions = {'.txt', '.md', '.pdf', '.docx', '.html', '.htm'}

    def load(self):
        """Load documents from file or directory."""
        if os.path.isdir(self.path):
            self.load_directory()
        elif os.path.isfile(self.path):
            self.load_file()
        else:
            raise ValueError("Provided path is neither a valid directory nor a supported file.")

    def load_file(self):
        """Load a single file with metadata."""
        file_path = self.path
        file_ext = Path(file_path).suffix.lower()
        
        if file_ext not in self.supported_extensions:
            raise ValueError(f"Unsupported file type: {file_ext}")
        
        content = self._extract_text(file_path, file_ext)
        if content:
            self.documents.append(content)
            
            # Create metadata
            metadata = DocumentMetadata(
                file_path=file_path,
                file_type=file_ext,
                last_modified=str(Path(file_path).stat().st_mtime),
                department=self._infer_department(file_path),
                category=self._infer_category(file_path)
            )
            self.metadata.append(metadata)

    def load_directory(self):
        """Load all supported files from directory."""
        for root, _, files in os.walk(self.path):
            for file in files:
                file_path = os.path.join(root, file)
                file_ext = Path(file).suffix.lower()
                
                if file_ext in self.supported_extensions:
                    try:
                        content = self._extract_text(file_path, file_ext)
                        if content:
                            self.documents.append(content)
                            
                            # Create metadata
                            metadata = DocumentMetadata(
                                file_path=file_path,
                                file_type=file_ext,
                                last_modified=str(Path(file_path).stat().st_mtime),
                                department=self._infer_department(file_path),
                                category=self._infer_category(file_path)
                            )
                            self.metadata.append(metadata)
                    except Exception as e:
                        print(f"Error loading {file_path}: {e}")
                        continue

    def _extract_text(self, file_path: str, file_ext: str) -> str:
        """Extract text from different file types."""
        if file_ext == '.txt' or file_ext == '.md':
            return self._extract_txt(file_path)
        elif file_ext == '.pdf':
            return self._extract_pdf(file_path)
        elif file_ext in ['.docx']:
            return self._extract_docx(file_path)
        elif file_ext in ['.html', '.htm']:
            return self._extract_html(file_path)
        else:
            return ""

    def _extract_txt(self, file_path: str) -> str:
        """Extract text from .txt or .md files."""
        with open(file_path, "r", encoding=self.encoding) as f:
            return f.read()

    def _extract_pdf(self, file_path: str) -> str:
        """Extract text from PDF files."""
        try:
            import PyPDF2
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
                return text
        except ImportError:
            print("PyPDF2 not installed. Install with: pip install PyPDF2")
            return ""
        except Exception as e:
            print(f"Error extracting PDF {file_path}: {e}")
            return ""

    def _extract_docx(self, file_path: str) -> str:
        """Extract text from DOCX files."""
        try:
            from docx import Document
            doc = Document(file_path)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            return text
        except ImportError:
            print("python-docx not installed. Install with: pip install python-docx")
            return ""
        except Exception as e:
            print(f"Error extracting DOCX {file_path}: {e}")
            return ""

    def _extract_html(self, file_path: str) -> str:
        """Extract text from HTML files."""
        try:
            from bs4 import BeautifulSoup
            with open(file_path, 'r', encoding=self.encoding) as file:
                soup = BeautifulSoup(file, 'html.parser')
                return soup.get_text()
        except ImportError:
            print("BeautifulSoup not installed. Install with: pip install beautifulsoup4")
            return ""
        except Exception as e:
            print(f"Error extracting HTML {file_path}: {e}")
            return ""

    def _infer_department(self, file_path: str) -> str:
        """Infer department from file path."""
        path_lower = file_path.lower()
        if 'hr' in path_lower or 'human' in path_lower:
            return 'hr'
        elif 'it' in path_lower or 'tech' in path_lower:
            return 'it'
        elif 'finance' in path_lower or 'accounting' in path_lower:
            return 'finance'
        elif 'legal' in path_lower or 'compliance' in path_lower:
            return 'legal'
        elif 'marketing' in path_lower or 'sales' in path_lower:
            return 'marketing'
        else:
            return 'general'

    def _infer_category(self, file_path: str) -> str:
        """Infer document category from file path."""
        path_lower = file_path.lower()
        if 'policy' in path_lower or 'procedure' in path_lower:
            return 'policy'
        elif 'faq' in path_lower or 'question' in path_lower:
            return 'faq'
        elif 'manual' in path_lower or 'guide' in path_lower:
            return 'manual'
        elif 'training' in path_lower or 'onboarding' in path_lower:
            return 'training'
        else:
            return 'document'

    def load_documents(self):
        """Load documents and return them with metadata."""
        self.load()
        return self.documents, self.metadata


class TextFileLoader:
    """Original text file loader for backward compatibility."""
    def __init__(self, path: str, encoding: str = "utf-8"):
        self.documents = []
        self.path = path
        self.encoding = encoding

    def load(self):
        if os.path.isdir(self.path):
            self.load_directory()
        elif os.path.isfile(self.path) and self.path.endswith(".txt"):
            self.load_file()
        else:
            raise ValueError(
                "Provided path is neither a valid directory nor a .txt file."
            )

    def load_file(self):
        with open(self.path, "r", encoding=self.encoding) as f:
            self.documents.append(f.read())

    def load_directory(self):
        for root, _, files in os.walk(self.path):
            for file in files:
                if file.endswith(".txt"):
                    with open(
                        os.path.join(root, file), "r", encoding=self.encoding
                    ) as f:
                        self.documents.append(f.read())

    def load_documents(self):
        self.load()
        return self.documents


class CharacterTextSplitter:
    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        assert (
            chunk_size > chunk_overlap
        ), "Chunk size must be greater than chunk overlap"

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self, text: str) -> List[str]:
        chunks = []
        for i in range(0, len(text), self.chunk_size - self.chunk_overlap):
            chunks.append(text[i : i + self.chunk_size])
        return chunks

    def split_texts(self, texts: List[str]) -> List[str]:
        chunks = []
        for text in texts:
            chunks.extend(self.split(text))
        return chunks


if __name__ == "__main__":
    loader = TextFileLoader("data/KingLear.txt")
    loader.load()
    splitter = CharacterTextSplitter()
    chunks = splitter.split_texts(loader.documents)
    print(len(chunks))
    print(chunks[0])
    print("--------")
    print(chunks[1])
    print("--------")
    print(chunks[-2])
    print("--------")
    print(chunks[-1])
