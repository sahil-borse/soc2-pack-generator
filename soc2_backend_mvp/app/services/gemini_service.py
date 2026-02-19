from google import genai
from app.config import settings


def gemini_generate_text(prompt: str) -> str:
    if not settings.GEMINI_API_KEY:
        raise Exception("GEMINI_API_KEY not configured")

    client = genai.Client(api_key=settings.GEMINI_API_KEY)

    response = client.models.generate_content(
        model=settings.GEMINI_MODEL,
        contents=prompt,
    )

    text = getattr(response, "text", None)
    if not text:
        return ""

    return text.strip()
