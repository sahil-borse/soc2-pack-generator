from datetime import datetime
from app.db import get_db


async def enable_framework_for_company(company_id: str, framework_id: str):
    db = get_db()

    # Check already enabled
    existing = await db.company_frameworks.find_one({
        "companyId": company_id,
        "frameworkId": framework_id
    })

    if existing:
        return {"message": "Framework already enabled"}

    # Insert into company_frameworks
    await db.company_frameworks.insert_one({
        "companyId": company_id,
        "frameworkId": framework_id,
        "enabledAt": datetime.utcnow(),
        "status": "active"
    })

    # Get all controls for this framework
    controls_cursor = db.controls.find({"frameworkId": framework_id})

    bulk = []

    async for c in controls_cursor:
        bulk.append({
            "companyId": company_id,
            "frameworkId": framework_id,
            "controlId": str(c["_id"]),
            "status": "not_started",
            "ownerUserId": None,
            "reviewFrequency": c.get("defaultReviewFrequency"),
            "lastReviewedAt": None,
            "createdAt": datetime.utcnow(),
            "updatedAt": datetime.utcnow(),
        })

    if bulk:
        await db.company_controls.insert_many(bulk)

    return {"message": "Framework enabled successfully"}