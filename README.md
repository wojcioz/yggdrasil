# yggdrasil

first pull the container before running docker compose up

docker pull ghcr.io/open-webui/open-webui:main




Backup docker


To reinstall WSL and Docker while preserving your Docker containers and volumes, you can follow these steps:

1. **Export Docker Containers and Volumes** : Before reinstalling WSL and Docker, export your Docker containers and volumes to ensure you can restore them later.
2. **Reinstall WSL and Docker** : Uninstall and reinstall WSL and Docker.
3. **Import Docker Containers and Volumes** : After reinstalling WSL and Docker, import your Docker containers and volumes.

### Step-by-Step Guide:

#### 1. Export Docker Containers and Volumes

1. **Export Docker Containers** : Use the `docker export` command to export your containers.


docker export -o vllm_container.tar vllm
docker export -o llamaindex_container.tar llamaindex
docker export -o open-webui_container.tar open-webui
docker export -o langgraph_container.tar langgraph
docker export -o flowise_container.tar flowise


1. **Export Docker Volumes** : Use the `docker run` command to create a backup of your volumes.



docker run --rm -v vllm:/volume -v E:/work/yggdrasil:/backup alpine tar czf /backup/vllm_volume.tar.gz -C /volume .
docker run --rm -v llamaindex:/volume -v E:/work/yggdrasil:/backup alpine tar czf /backup/llamaindex_volume.tar.gz -C /volume .
docker run --rm -v open-webui:/volume -v E:/work/yggdrasil:/backup alpine tar czf /backup/open-webui_volume.tar.gz -C /volume .
docker run --rm -v langgraph:/volume -v E:/work/yggdrasil:/backup alpine tar czf /backup/langgraph_volume.tar.gz -C /volume .
docker run --rm -v flowise:/volume -v E:/work/yggdrasil:/backup alpine tar czf /backup/flowise_volume.tar.gz -C /volume .

#### 2. Reinstall WSL and Docker

1. **Uninstall WSL** : Follow the instructions to uninstall WSL from your system.
2. **Uninstall Docker** : Follow the instructions to uninstall Docker from your system.
3. **Reinstall WSL** : Follow the instructions to reinstall WSL on your system.
4. **Reinstall Docker** : Follow the instructions to reinstall Docker on your system.

#### 3. Import Docker Containers and Volumes

1. **Import Docker Containers** : Use the `docker import` command to import your containers.
docker import vllm_container.tar vllm
docker import llamaindex_container.tar llamaindex
docker import open-webui_container.tar open-webui

docker import langgraph_container.tar langgraph
docker import flowise_container.tar flowise

1. **Import Docker Volumes** : Use the `docker run` command to restore your volumes.

docker volume create vllm_volume
docker run --rm -v vllm_volume:/volume -v $(pwd):/backup alpine tar xzf /backup/vllm_volume.tar.gz -C /volume

docker volume create llamaindex_volume
docker run --rm -v llamaindex_volume:/volume -v $(pwd):/backup alpine tar xzf /backup/llamaindex_volume.tar.gz -C /volume

docker volume create open-webui_volume
docker run --rm -v open-webui_volume:/volume -v $(pwd):/backup alpine tar xzf /backup/open-webui_volume.tar.gz -C /volume

1. **Update Docker Compose Configuration** : Ensure your Docker Compose configuration uses the restored volumes.
version: '3.8'

services:
  # vLLM - LLM inference service with the smallest model
  vllm:
    build:
      context: ./vllm
      dockerfile: Dockerfile
    container_name: vllm
    runtime: nvidia
    deploy:
      resources:
        reservations:
          devices:
            - capabilities: [ gpu ]
    ports:
      - "8000:8000"
    volumes:
      - vllm_volume:/app
      - ~/.cache/huggingface:/root/.cache/huggingface
      - ./chat_template.yaml:/app/chat_template.yaml # Mount the chat template file
    ipc: host
    secrets:
      - huggingface_key

  # LlamaIndex - For RAG handling
  llamaindex:
    image: python:3.9-slim
    container_name: llamaindex
    command: >
      bash -c "pip install llama-index llama-index-vector-stores-chroma openai && export OPENAI_API_KEY=$(cat /run/secrets/openai_api_key) && python3 -m llama_index.run"
    ports:
      - "5001:5000"
    volumes:
      - llamaindex_volume:/app/docs
    secrets:
      - openai_api_key

  # Open WebUI - Chat interface
  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    container_name: open-webui
    ports:
      - "3000:8080"
    volumes:
      - open-webui_volume:/app/backend/data
      - ./chat_template.yaml:/app/chat_template.yaml # Mount the chat template file
    environment:
      - API_URL=http://vllm:8000/v1
      - 'OPENAI_API_BASE_URL=http://vllm:8000/v1'
      - ENABLE_RAG_WEB_SEARCH=true
      - RAG_WEB_SEARCH_ENGINE=duckduckgo
      - CHAT_TEMPLATE=/app/chat_template.yaml # Set the chat template path

secrets:
  huggingface_key:
    file: ./hf_key.txt

volumes:
  vllm_volume:
  llamaindex_volume:
  open-webui_volume:

networks:
  default:
    name: llm-rag-network

1. **Build and Run the Docker Compose Setup** : Build and run your Docker Compose setup to ensure everything is restored correctly.

docker-compose up --build

By following these steps, you can reinstall WSL and Docker while preserving your Docker containers and volumes.
