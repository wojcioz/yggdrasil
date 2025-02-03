import os
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores import ChromaVectorStore
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize ChromaVectorStore
chroma_api_url = os.getenv("CHROMA_API_URL", "http://localhost:8800")
vector_store = ChromaVectorStore(api_url=chroma_api_url)

# Initialize GPTVectorStoreIndex
index = GPTVectorStoreIndex(vector_store=vector_store)


@app.route("/index", methods=["POST"])
def index_documents():
    data = request.json
    documents = data.get("documents", [])
    for doc in documents:
        index.add_document(doc)
    return jsonify({"status": "success"}), 200


@app.route("/query", methods=["POST"])
def query_index():
    data = request.json
    query = data.get("query", "")
    results = index.query(query)
    return jsonify(results), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
