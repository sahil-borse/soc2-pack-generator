from fastapi import APIRouter, Depends

from ..models.company_profile_model import CompanyProfileUpsert
from ..services.company_profile_service import get_company_profile, upsert_company_profile
from ..services.document_service import get_current_user_id

router = APIRouter(prefix="/api/company-profile", tags=["company-profile"])


@router.get("")
async def get_profile(user_id: str = Depends(get_current_user_id)):
    return await get_company_profile(user_id)


@router.put("")
async def put_profile(payload: CompanyProfileUpsert, user_id: str = Depends(get_current_user_id)):
    return await upsert_company_profile(user_id, payload.profile)
