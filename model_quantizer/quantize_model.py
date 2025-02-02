from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the model and tokenizer
model_name = "mistralai/Mistral-7B-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to(device)

# Quantize the model
quantized_model = torch.quantization.quantize_dynamic(
    model, {torch.nn.Linear}, dtype=torch.qint8
)

# Save the quantized model
quantized_model.save_pretrained("/models/quantized_mistral_7b")
tokenizer.save_pretrained("/models/quantized_mistral_7b")

print("Model quantization complete and saved to /models/quantized_mistral_7b")
