from modules.vector_store import create_vector_store
from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from modules.chat_history import message_history
from langchain_core.prompts import ChatPromptTemplate

#  Create FAISS retriever once
retriever = create_vector_store()

#  Initialize Memory for Chat History
memory = ConversationBufferMemory(
    memory_key="chat_history",
    output_key="answer",
    chat_memory=message_history,
    return_messages=True,
)

#  Initialize Groq LLM
llm = ChatGroq(model_name="mixtral-8x7b-32768")

#   Strict Prompt to Stop LLM Hallucinations
strict_prompt = ChatPromptTemplate.from_messages([
    ("system", """
        You are an AI assistant named **Div**, designed to assist users with inquiries **strictly related to the company**.  
        **You must only provide answers based on the retrieved company information below.**  
        **If the user's question is unrelated to the company, simply say:**
        **"I only provide company-related information."**  

        **STRICT RULES FOR ANSWERING QUERIES:**  
        - Use **only the provided company data**—do not generate answers from external sources.  
        - If the retrieved company data **does not contain an answer**, simply reply:  
          **"I don't have information on that topic."**  
        - Never assume, guess, or speculate.  

        ### ** Retrieved Company Information:**
        {context}

        ---  
        * User Query:**  
        {question}  
    """),
    ("user", "{question}")
])

#  Create Conversational RAG Chain with Strict Prompt
rag_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    memory=memory,
    return_source_documents=True,
    combine_docs_chain_kwargs={"prompt": strict_prompt}  #  Enforce strict mode
)

def chat_with_groq(query):
    """Processes user query and retrieves relevant company information using RAG."""
    
    # Invoke the RAG chain with chat history
    result = rag_chain.invoke({"question": query})

    #  Extract only the AI response
    return result["answer"] if "answer" in result else " Error: No valid response found."
