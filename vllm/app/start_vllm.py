# filepath: /home/wojcioz/yggdrasil/vllm/start_vllm.py
import os
import subprocess

# Set environment variables
os.environ["HUGGING_FACE_HUB_TOKEN"] = open("/run/secrets/huggingface_key").read().strip()

# Define the command to run the vllm service
command = [
    "python3",
    "api_server.py",
    "--model", "mistralai/Mistral-7B-v0.1",
    "--chat-template", "/app/chat_template.yaml"
]

# Run the command
subprocess.run(command)
