import os
import streamlit as st
from modules.app import chat_with_groq

#  Set Streamlit Page Configuration
st.set_page_config(
    page_title="DataVerze AI Assistant",
    layout="wide"
)

def main():
    """Runs the Streamlit frontend."""

    #  Sidebar (About Us)
    with st.sidebar:
        # st.markdown("<h2 style='text-align: center; font-family: Arial, sans-serif;'>📌 About DataVerze</h2>", unsafe_allow_html=True)
        
        #  Placeholder for Image 
        image_path = "data/company_logo.jpg"  
        if os.path.exists(image_path):
            st.image(image_path, width=100)  # Set width to 200px (adjust as needed)

        
        st.markdown("""
        <div style="font-family: Arial, sans-serif; font-size: 15px; line-height: 1.5;">
        Welcome to <b>DataVerze AI Assistant</b>, your intelligent chatbot for all company-related queries.
        
        🔹 <b>Use Cases:</b>
        - Get instant, accurate responses about DataVerze.  
        - Designed for employees, clients, and customers.  
        - Provides information on policies, services, and general details.  
        - Ensures responses are strictly <b>company-related</b> with no speculation.  
        </div>
        """, unsafe_allow_html=True)

    #  Main Chatbot Interface
    st.markdown("<h1 style='text-align: center; font-family: Arial, sans-serif;'> DataVerze AI Chat</h1>", unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: center; font-size: 16px; font-family: Arial, sans-serif;'>Ask me anything about DataVerze, and I’ll provide accurate responses based on company data.</p>", unsafe_allow_html=True)

    #  Chat Input Box
    user_input = st.text_input("🔍 Ask about DataVerze:")

    #  If user inputs a query, fetch response
    if user_input:
        try:
            response = chat_with_groq(user_input)
            st.markdown("<h3>🗨 AI Response:</h3>", unsafe_allow_html=True)
            st.success(response)  #  Shows response in a highlighted box
        except Exception as e:
            st.error(f" Error: {str(e)}")  # Show errors in Streamlit

    #  Footer
    st.markdown("---")
    st.markdown("<p style='text-align: center; font-size: 14px; font-family: Arial, sans-serif;'>© <b>DataVerze AI Assistant - All Rights Reserved 2025</b></p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

