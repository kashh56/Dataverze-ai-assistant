from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from modules.document_loader import load_documents

def create_vector_store():
    """Processes documents and creates a FAISS vector database with properly sized chunks."""
    docs = load_documents()

    # Smarter text splitting that respects paragraph/sentence boundaries but enforces 500-character max
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, 
        chunk_overlap=50,  
        separators=["\n\n", "\n", " ", ""],  # First try paragraphs, then sentences, then spaces, finally characters
    )

    texts = text_splitter.split_documents(docs)

    # Use Hugging Face embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Create FAISS vector store
    vector_db = FAISS.from_documents(texts, embeddings)
    
    return vector_db.as_retriever()
