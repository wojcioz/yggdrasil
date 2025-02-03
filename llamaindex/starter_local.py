from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings

from llama_index.embeddings import HuggingFaceEmbedding
from llama_index.llms import Ollama
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    ServiceContext,
    PromptTemplate,
)

# from llama_index.llms.huggingface import HuggingFaceLLM
# Load documents
documents = SimpleDirectoryReader("data").load_data()

# Set embedding model
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# Set LLM
Settings.llm = Ollama(model="llama3", request_timeout=360.0)

# Create index
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

# Query the index
response = query_engine.query("What did the author do growing up?")
print(response)
