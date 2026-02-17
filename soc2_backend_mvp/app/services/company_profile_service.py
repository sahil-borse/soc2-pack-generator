from datetime import datetime, timezone

from ..db import get_db


async def get_company_profile(user_id: str):
    db = get_db()
    doc = await db.company_profiles.find_one({"userId": user_id})
    if not doc:
        return {"profile": {}}

    return {
        "id": str(doc["_id"]),
        "userId": doc["userId"],
        "profile": doc.get("profile", {}),
        "updatedAt": doc.get("updatedAt"),
    }


async def upsert_company_profile(user_id: str, profile: dict):
    db = get_db()
    now = datetime.now(timezone.utc)

    await db.company_profiles.update_one(
        {"userId": user_id},
        {"$set": {"profile": profile, "updatedAt": now}},
        upsert=True,
    )

    return await get_company_profile(user_id)
