from fastapi import Header, Depends, HTTPException
from app.services.document_service import get_current_user_id
from app.db import get_db


async def get_company_context(
    x_company_id: str = Header(...),
    user_id: str = Depends(get_current_user_id),
):
    db = get_db()

    membership = await db.company_memberships.find_one({
        "companyId": x_company_id,
        "userId": user_id
    })

    if not membership:
        raise HTTPException(status_code=403, detail="Not part of this company")

    return membership