FROM nvidia/cuda:11.7.1-cudnn8-runtime-ubuntu22.04

# Install Python and necessary packages
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install transformers torch

# Copy the quantization script
COPY quantize_model.py /app/quantize_model.py

# Set the working directory
WORKDIR /app