# filepath: /home/wojcioz/yggdrasil/download_model.py
import os
import requests

MODEL_NAME = os.getenv("MODEL_NAME", "TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF")
MODEL_URL = f"https://example.com/path/to/{MODEL_NAME}/model/file"  # Replace with actual model URL
MODEL_DIR = f"/models/{MODEL_NAME}"

os.makedirs(MODEL_DIR, exist_ok=True)

model_file_path = os.path.join(MODEL_DIR, "model_file")

if not os.path.exists(model_file_path):
    print(f"Downloading model {MODEL_NAME}...")
    response = requests.get(MODEL_URL)
    with open(model_file_path, "wb") as f:
        f.write(response.content)
    print(f"Model {MODEL_NAME} downloaded successfully.")
else:
    print(f"Model {MODEL_NAME} already exists.")
