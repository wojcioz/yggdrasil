import os
import fitz  # PyMuPDF
import requests

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def index_docs():
    # Directory containing PDF documents
    docs_dir = "/app/docs"

    # Prepare documents for indexing
    documents = []
    for filename in os.listdir(docs_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(docs_dir, filename)
            text = extract_text_from_pdf(pdf_path)
            documents.append({"id": filename, "text": text})
            print(f"Indexed document: {filename}")

    # Index documents
    index_url = "http://chromadb:8000/index"
    index_payload = {"documents": documents}
    index_response = requests.post(index_url, json=index_payload)
    print("Index Response:", index_response.json())

    # Query documents
    query_url = "http://chromadb:8000/query"
    query_payload = {"query": "Find documents related to text"}
    query_response = requests.post(query_url, json=query_payload)
    print("Query Response:", query_response.json())