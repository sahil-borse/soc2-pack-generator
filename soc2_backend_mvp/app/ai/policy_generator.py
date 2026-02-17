from ..config import settings
from .openai_client import get_openai_client
from .prompts import SYSTEM_PROMPT, build_policy_prompt


async def generate_policy_markdown(policy_name: str, company_profile: dict) -> str:
    client = get_openai_client()
    prompt = build_policy_prompt(policy_name, company_profile)

    res = await client.chat.completions.create(
        model=settings.OPENAI_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=0.35,
    )

    return res.choices[0].message.content or ""
