from fastapi import APIRouter, Depends
from .models import UpdateBoardConfigRequest
from .service import update_board_config, get_board_config
from app.core.company_context import get_company_context

router = APIRouter(prefix="/api/board-config", tags=["Board Config"])


@router.get("")
async def get_config(frameworkId: str, membership=Depends(get_company_context)):
    company_id = membership["companyId"]
    return await get_board_config(company_id, frameworkId)


@router.post("")
async def update_config(payload: UpdateBoardConfigRequest, membership=Depends(get_company_context)):
    company_id = membership["companyId"]
    return await update_board_config(company_id, payload.frameworkId, payload.columns)