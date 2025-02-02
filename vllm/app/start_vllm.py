# import os
# import subprocess
# from transformers import AutoModelForCausalLM, AutoTokenizer
# import bitsandbytes as bnb

# # Set environment variables
# os.environ["HUGGING_FACE_HUB_TOKEN"] = open("/run/secrets/huggingface_key").read().strip()

# # Define the model name
# model_name = "mistralai/Mistral-7B-v0.1"

# # Load the model and tokenizer
# model = AutoModelForCausalLM.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)

# # Quantize the model
# quantized_model = bnb.nn.quantization.quantize_model(model, dtype=bnb.float16)

# # Save the quantized model
# quantized_model.save_pretrained("/app/quantized_model")
# tokenizer.save_pretrained("/app/quantized_model")

# # Define the command to run the vllm service
# command = [
#     "python3",
#     "api_server.py",
#     "--model", "/app/quantized_model",
#     "--chat-template", "/app/chat_template.yaml"
# ]

# # Run the command
# subprocess.run(command)


from vllm import LLM, SamplingParams

prompts = [
    "Hello, my name is",
    "The president of the United States is",
    "The capital of France is",
    "The future of AI is",
]

# initialize
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
llm = LLM(model="facebook/opt-125m")

# perform the inference
outputs = llm.generate(prompts, sampling_params)

# print outputs
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")