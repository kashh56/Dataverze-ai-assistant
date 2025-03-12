### Welcome to dataverse.ai
This is a Retrieval-Augmented Generation (RAG) chatbot that answers only company-related questions.


# Component	                Purpose
app.py  	                Manages chatbot logic, invokes RAG pipeline, formats responses
document_loader.py	        Loads company info from info.txt
chat_history.py	            Maintains chat memory for multi-turn conversations
vector_store.py	            Creates & manages FAISS vector database for fast retrieval

## How It Works
1️ User asks a question in Streamlit frontend.
2️ Retriever fetches the most relevant document chunks from FAISS.
3️ Chatbot formats the retrieved text + query into a structured prompt.
4️ Groq's Mixtral-8x7B generates a response based only on retrieved content.
5️ Response is displayed to the user while storing chat history.

 ## Key Features
Fast Vector Search using FAISS
Strict Company-Focused Responses (No hallucination)
Multi-Turn Chat with Memory
Highly Scalable & Portable

