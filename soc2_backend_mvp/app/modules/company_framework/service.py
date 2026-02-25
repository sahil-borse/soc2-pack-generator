from app.db import get_db
from app.modules.company_controls.service import calculate_framework_score
from bson import ObjectId


async def list_company_frameworks(company_id: str):
    db = get_db()

    frameworks = []
    cursor = db.company_frameworks.find({
        "companyId": company_id,
        "status": "active"
    })

    async for f in cursor:
        framework = await db.frameworks.find_one({
            "_id": ObjectId(f["frameworkId"])
        })

        if not framework:
            continue  # safety guard

        score = await calculate_framework_score(company_id, f["frameworkId"])

        frameworks.append({
            "frameworkId": f["frameworkId"],
            "name": framework["name"],
            "code": framework["code"],
            "score": score
        })

    return frameworks