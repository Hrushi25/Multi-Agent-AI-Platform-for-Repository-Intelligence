from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_ENV: str = os.getenv("APP_ENV", "dev")
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GITHUB_TOKEN: str = os.getenv("GITHUB_TOKEN", "")

settings = Settings()
