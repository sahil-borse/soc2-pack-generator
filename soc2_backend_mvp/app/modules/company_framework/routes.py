from fastapi import APIRouter, Depends
from app.core.company_context import get_company_context
from .service import list_company_frameworks

router = APIRouter(prefix="/api/company-frameworks", tags=["Company Frameworks"])


@router.get("")
async def get_company_frameworks(
    membership = Depends(get_company_context)
):
    company_id = membership["companyId"]
    return await list_company_frameworks(company_id)