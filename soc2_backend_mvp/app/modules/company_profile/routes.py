from fastapi import APIRouter, Depends
from datetime import datetime
from bson import ObjectId

from app.db import get_db
from app.core.company_context import get_company_context
from app.models.company_profile_model import CompanyProfileUpsert

router = APIRouter(prefix="/api/company-profile", tags=["Company Profile"])


@router.get("")
async def get_company_profile(
    membership = Depends(get_company_context)
):
    company_id = membership["companyId"]
    db = get_db()

    profile = await db.company_profiles.find_one({"companyId": company_id})

    if not profile:
        return {}

    return {
        "id": str(profile["_id"]),
        "companyId": profile["companyId"],
        "profile": profile["profile"],
    }


@router.put("")
async def upsert_company_profile(
    payload: CompanyProfileUpsert,
    membership = Depends(get_company_context)
):
    company_id = membership["companyId"]
    db = get_db()

    existing = await db.company_profiles.find_one({"companyId": company_id})

    if existing:
        await db.company_profiles.update_one(
            {"companyId": company_id},
            {"$set": {
                "profile": payload.profile,
                "updatedAt": datetime.utcnow()
            }}
        )
    else:
        await db.company_profiles.insert_one({
            "companyId": company_id,
            "profile": payload.profile,
            "createdAt": datetime.utcnow(),
            "updatedAt": datetime.utcnow()
        })

    return {"ok": True}