from datetime import datetime
from bson import ObjectId
from app.db import get_db


async def create_company(user_id: str, name: str):
    db = get_db()

    company = {
        "name": name,
        "createdBy": user_id,
        "createdAt": datetime.utcnow(),
        "updatedAt": datetime.utcnow(),
    }

    result = await db.companies.insert_one(company)
    company_id = str(result.inserted_id)

    membership = {
        "companyId": company_id,
        "userId": user_id,
        "role": "company_admin",
        "createdAt": datetime.utcnow(),
    }

    await db.company_memberships.insert_one(membership)

    return {
        "id": company_id,
        "name": name,
        "role": "company_admin",
        "createdAt": company["createdAt"],
    }


async def get_user_companies(user_id: str):
    db = get_db()

    memberships = db.company_memberships.find({"userId": user_id})
    results = []

    async for m in memberships:
        company = await db.companies.find_one({"_id": ObjectId(m["companyId"])})
        if company:
            results.append({
                "id": str(company["_id"]),
                "name": company["name"],
                "role": m["role"],
                "createdAt": company["createdAt"],
            })

    return results
