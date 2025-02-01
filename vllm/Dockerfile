# Dockerfile.vllm
FROM vllm/vllm-openai:latest

# Install Python and necessary packages
RUN apt-get update && apt-get install -y python3 python3-pip

# Copy the Python script into the container
COPY app/download_model_transformers.py /app/download_model_transformers.py

# Install transformers library
RUN pip3 install transformers

# Set environment variables
ENV MODEL_NAME=TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF
ENV TENSOR_PARALLEL_SIZE=1

# Set the working directory
WORKDIR /app

# Command to run your application
# CMD ["python3", "/app/download_model_transformers.py"]
