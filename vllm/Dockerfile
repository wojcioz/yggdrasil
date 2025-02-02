# Dockerfile.vllm
FROM vllm/vllm-openai:latest

# Install Python and necessary packages
RUN apt-get update && apt-get install -y python3 python3-pip

# Copy the Python script into the container
# COPY app/download_model_transformers.py /app/download_model_transformers.py

# Install transformers library
RUN pip3 install transformers

# Set environment variables

# Set the working directory
WORKDIR /app

# Command to run your application
# CMD ["python3", "/app/download_model_transformers.py"]

# ENTRYPOINT ["python3", "start_vllm.py"]
# ENTRYPOINT ["tail", "-f", "/dev/null"]