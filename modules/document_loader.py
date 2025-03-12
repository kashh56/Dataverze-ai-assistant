import os
from langchain_core.documents import Document

FILE_PATH =  os.path.join("data", "info.txt")

def load_documents():
    """Loads and returns text from info.txt as a LangChain document."""
    if not os.path.exists(FILE_PATH):
        raise FileNotFoundError(f" Error: {FILE_PATH} not found.")

    with open(FILE_PATH, "r", encoding="utf-8") as f:
        file_content = f.read().strip()

    if not file_content:
        raise ValueError("Error: info.txt is empty. Please add company-related content.")

    return [Document(page_content=file_content)]
