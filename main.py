import streamlit as st
from llama_index.llms import OpenAI
from llama_index import VectorStoreIndex, SimpleDirectoryReader

# documents = SimpleDirectoryReader("test").load_data()

# index = VectorStoreIndex.from_documents(documents)

# query_engine = index.as_query_engine(streaming=True)
# chat_engine = index.as_chat_engine()

# response = query_engine.query("Write a story about bob.")
# response.print_response_stream()

def SaveKey():
    with open(".env", "w", encoding="utf-8") as env:
        env.write("OPENAI_API_KEY = " + openai_api_key)


with st.sidebar:
    api_text_input = st.empty()
    openai_api_key = api_text_input.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    api_text_input.text_input("OpenAI API Key", key="chatbot_api_key", type="password", value=openai_api_key)
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    st.button("Save Key", on_click=SaveKey())