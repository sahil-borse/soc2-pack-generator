from fastapi import APIRouter, Depends
from .models import CreateCompanyRequest
from .service import create_company
from app.services.document_service import get_current_user_id

router = APIRouter(prefix="/api/companies", tags=["Companies"])


@router.post("")
async def create_company_route(
    payload: CreateCompanyRequest,
    user_id: str = Depends(get_current_user_id)
):
    return await create_company(payload.name, user_id)