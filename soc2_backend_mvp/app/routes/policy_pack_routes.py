from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
import io

from app.services.document_service import get_current_user_id
from app.services.company_profile_service import get_company_profile
from app.services.policy_pack_service import generate_policy_pack_zip

router = APIRouter(prefix="/api/policy-pack", tags=["Policy Pack"])


@router.post("/generate")
async def generate_pack(user_id: str = Depends(get_current_user_id)):
    profile_doc = await get_company_profile(user_id)

    if not profile_doc:
        raise HTTPException(status_code=400, detail="Company profile not found")

    zip_bytes = generate_policy_pack_zip(profile_doc["profile"])

    return StreamingResponse(
        io.BytesIO(zip_bytes),
        media_type="application/zip",
        headers={"Content-Disposition": "attachment; filename=soc2_policy_pack.zip"},
    )
