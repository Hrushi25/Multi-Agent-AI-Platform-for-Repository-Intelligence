from google import genai
from app.config import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

# List all available models
models = client.models.list()
for model in models:
    print(f"Model: {model.name}")