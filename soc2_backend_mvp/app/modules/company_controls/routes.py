from fastapi import APIRouter, Depends
from .models import UpdateCompanyControlRequest
from .service import update_company_control, calculate_framework_score, list_company_controls
from app.core.company_context import get_company_context

router = APIRouter(prefix="/api/company-controls", tags=["Company Controls"])


@router.patch("/{control_id}")
async def update_control(
    control_id: str,
    payload: UpdateCompanyControlRequest,
    membership = Depends(get_company_context)
):
    company_id = membership["companyId"]
    return await update_company_control(control_id, company_id, payload.dict(exclude_none=True))


@router.get("/score")
async def get_score(
    frameworkId: str,
    membership = Depends(get_company_context)
):
    company_id = membership["companyId"]
    score = await calculate_framework_score(company_id, frameworkId)
    return {"score": score}

@router.get("")
async def list_controls(
    frameworkId: str,
    membership = Depends(get_company_context)
):
    company_id = membership["companyId"]
    return await list_company_controls(company_id, frameworkId)