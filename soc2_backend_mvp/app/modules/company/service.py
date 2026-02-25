from datetime import datetime
from app.db import get_db


async def create_company(name: str, user_id: str):
    db = get_db()

    company = {
        "name": name,
        "createdAt": datetime.utcnow(),
        "updatedAt": datetime.utcnow()
    }

    result = await db.companies.insert_one(company)

    company_id = str(result.inserted_id)

    # create membership
    await db.company_memberships.insert_one({
        "companyId": company_id,
        "userId": user_id,
        "role": "owner",
        "createdAt": datetime.utcnow()
    })

    return {
        "id": company_id,
        "name": name
    }