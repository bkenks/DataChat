
from llama_index.llms import OpenAI
from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("test").load_data()

index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine(streaming=True)
chat_engine = index.as_chat_engine()

response = query_engine.query("Write a story about bob.")
response.print_response_stream()