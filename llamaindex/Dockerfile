FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set environment variables
ENV CHROMA_API_URL=http://localhost:8800

# Command to run the application
CMD ["bash", "-c", "pip install -r requirements.txt && export OPENAI_API_KEY=$(cat /run/secrets/openai_api_key) && python3 /app/starter_local.py"]