# filepath: /home/wojcioz/yggdrasil/vllm/start_vllm.py
import os
import subprocess
from transformers import AutoModelForCausalLM, AutoTokenizer
import bitsandbytes as bnb

# Set environment variables
os.environ["HUGGING_FACE_HUB_TOKEN"] = open("/run/secrets/huggingface_key").read().strip()

# Define the model name
model_name = "mistralai/Mistral-7B-v0.1"

# Load the model and tokenizer
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Quantize the model
quantized_model = bnb.nn.quantization.quantize_model(model, dtype=bnb.float16)

# Save the quantized model
quantized_model.save_pretrained("/app/quantized_model")
tokenizer.save_pretrained("/app/quantized_model")

# Define the command to run the vllm service
command = [
    "python3",
    "api_server.py",
    "--model", "/app/quantized_model",
    "--chat-template", "/app/chat_template.yaml"
]

# Run the command
subprocess.run(command)
