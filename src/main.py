import streamlit as st
from ui import render_wiki_interface, display_response
from ollama_service import chat_with_ollama

def main():
    st.set_page_config(page_title="OLLAMA Wikipedia", page_icon="📚", layout="wide")
    
    user_query = render_wiki_interface()
    
    if user_query:
        with st.spinner("Generating response..."):
            response = chat_with_ollama(user_query)
        display_response(user_query, response)

if __name__ == "__main__":
    main()
