# yggdrasil

first pull the container before running docker compose up

docker pull ghcr.io/open-webui/open-webui:main

# download a model
git lfs install

git clone https://huggingface.co/neuralmagic/Mistral-7B-Instruct-v0.3-quantized.w8a16


## Work Breakdown Structure (WBS)

1️⃣ **LLM Inference & Adapter Setup (vLLM)**
- [x] Set up vLLM with base model
- [ ] Load LoRA adapters and implement dynamic switching
- [X] Expose an OpenAI-compatible API for interaction

2️⃣ **RAG & Retrieval Pipeline (LangGraph + LlamaIndex + ChromaDB)**
- [x] Set up ChromaDB for document storage
- [ ] Configure LlamaIndex to index and retrieve documents
- [ ] Use LangGraph to dynamically decide when to retrieve documents vs. when to generate purely from the model
- [ ] Optimize retrieval strategies (hybrid search, reranking, etc.)

3️⃣ **Chatbot Logic (LangGraph)**
- [ ] Create modular LangGraph workflows for different use cases
- [ ] Implement different user intents (e.g., direct model queries vs. RAG-assisted queries)
- [ ] Add post-processing steps (e.g., response validation, ranking)

4️⃣ **Web API & User Interface**
- [ ] Build a FastAPI-based backend to expose chat endpoints
- [ ] Create a lightweight React-based Web UI for chat interactions
- [ ] Integrate UI with the LangGraph backend for dynamic interactions

5️⃣ **Optimization & Deployment**
- [ ] Benchmark vLLM inference performance
- [ ] Tune vector search (ChromaDB) for optimal RAG response speed
- [ ] Implement caching and response memory for contextual conversations
- [ ] Secure API endpoints and authentication