from google import genai
from app.config import settings


def get_gemini_client() -> genai.Client:
    if not settings.GEMINI_API_KEY:
        raise Exception("GEMINI_API_KEY not configured")
    return genai.Client(api_key=settings.GEMINI_API_KEY)
