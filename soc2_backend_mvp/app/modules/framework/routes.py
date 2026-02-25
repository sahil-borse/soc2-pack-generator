from fastapi import APIRouter, Depends
from .models import CreateFrameworkRequest
from .service import create_framework, list_frameworks
from app.core.company_context import get_company_context
from .activation_service import enable_framework_for_company

router = APIRouter(prefix="/api/frameworks", tags=["Frameworks"])


@router.post("")
async def create_framework_route(payload: CreateFrameworkRequest):
    return await create_framework(payload.dict())


@router.get("")
async def get_frameworks():
    return await list_frameworks()

@router.post("/enable")
async def enable_framework(
    frameworkId: str,
    membership = Depends(get_company_context)
):
    company_id = membership["companyId"]
    return await enable_framework_for_company(company_id, frameworkId)