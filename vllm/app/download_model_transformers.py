import os
from transformers import AutoModelForCausalLM, AutoTokenizer

# Get the model name from the environment variable
model_name = os.getenv("MODEL_NAME", "fallback_model_name")  # Replace "default_model_name" with a fallback model name if needed

# Load the model and tokenizer from Hugging Face
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Save the model to the "models" folder
model.save_pretrained("./models")
tokenizer.save_pretrained("./models")

print(f"Model {model_name} downloaded and saved successfully.")