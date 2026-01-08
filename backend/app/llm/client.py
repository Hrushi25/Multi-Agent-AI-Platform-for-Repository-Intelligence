from google import genai
from app.config import settings

if not settings.GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY not set")

client = genai.Client(api_key=settings.GEMINI_API_KEY)

class GeminiClient:
    def __init__(self, model_name: str = "models/gemini-2.5-flash"):
        self.model_name = model_name

    def generate(self, prompt: str) -> str:
        response = client.models.generate_content(
            model=self.model_name,
            contents=prompt,
        )
        return response.text.strip()