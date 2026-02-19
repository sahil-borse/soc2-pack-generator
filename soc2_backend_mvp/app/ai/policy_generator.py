from ..config import settings
from .prompts import SYSTEM_PROMPT, build_policy_prompt
from app.services.gemini_service import gemini_generate_text


async def generate_policy_markdown(policy_name: str, company_profile: dict) -> str:
    prompt = build_policy_prompt(policy_name, company_profile)

    final_prompt = f"""
{SYSTEM_PROMPT}

USER REQUEST:
{prompt}
""".strip()

    text = gemini_generate_text(final_prompt)

    return text or ""
