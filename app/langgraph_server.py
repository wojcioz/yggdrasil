import langgraph
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

VLLM_API = "http://vllm:8000/v1"
LLAMAINDEX_API = "http://llamaindex:5000"

# Function to classify user query type
def classify_query(inputs):
    query = inputs["query"]
    if "finance" in query.lower():
        return "finance_adapter"
    elif "tech" in query.lower():
        return "tech_adapter"
    else:
        return "default_adapter"

# Function to fetch documents using LlamaIndex
def retrieve_documents(inputs):
    query = inputs["query"]
    response = requests.post(f"{LLAMAINDEX_API}/retrieve", json={"query": query})
    return {"retrieved_docs": response.json()}

# Function to call vLLM
def call_vllm(inputs):
    model = inputs["adapter"]
    query = inputs["query"]
    response = requests.post(f"{VLLM_API}/chat/completions", json={"model": model, "messages": [{"role": "user", "content": query}]})
    return {"response": response.json()}

# Create LangGraph workflow
graph = langgraph.Graph()
graph.add_node("classify_query", classify_query)
graph.add_node("retrieve_documents", retrieve_documents)
graph.add_node("call_vllm", call_vllm)

graph.add_edge("classify_query", "retrieve_documents")
graph.add_edge("retrieve_documents", "call_vllm")

executor = langgraph.Executor(graph)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    result = executor.invoke({"query": data["query"]})
    return jsonify(result["response"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)