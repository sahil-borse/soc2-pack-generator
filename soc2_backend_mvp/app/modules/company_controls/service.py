from app.db import get_db
from bson import ObjectId


async def update_company_control(control_id: str, company_id: str, data: dict):
    db = get_db()

    await db.company_controls.update_one(
        {
            "_id": ObjectId(control_id),
            "companyId": company_id
        },
        {"$set": data}
    )

    updated = await db.company_controls.find_one({
        "_id": ObjectId(control_id)
    })

    return {
        "id": str(updated["_id"]),
        "status": updated["status"]
    }


async def calculate_framework_score(company_id: str, framework_id: str):
    db = get_db()

    total = await db.company_controls.count_documents({
        "companyId": company_id,
        "frameworkId": framework_id
    })

    implemented = await db.company_controls.count_documents({
        "companyId": company_id,
        "frameworkId": framework_id,
        "status": "implemented"
    })

    if total == 0:
        return 0

    return round((implemented / total) * 100, 2)


async def list_company_controls(company_id: str, framework_id: str):
    db = get_db()

    company_controls = await db.company_controls.find({
        "companyId": company_id,
        "frameworkId": framework_id
    }).to_list(None)

    result = []

    for cc in company_controls:
        control = await db.controls.find_one({
            "_id": ObjectId(cc["controlId"])
        })

        if not control:
            continue

        result.append({
            "id": str(cc["_id"]),
            "controlCode": control.get("controlCode"),
            "title": control.get("title"),
            "category": control.get("category"),
            "status": cc.get("status", "not_started"),
        })

    return result