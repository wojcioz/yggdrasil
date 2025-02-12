# Dockerfile
FROM python:3.12

# Install necessary packages
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install ChromaDB and Jupyter
RUN pip install --no-cache-dir chromadb jupyter ipykernel pymupdf sentence_transformers

# Create a directory for the app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Expose the Jupyter port
EXPOSE 8888

# Run Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]