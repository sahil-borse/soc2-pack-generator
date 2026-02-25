from fastapi import APIRouter, Query
from .models import CreateControlRequest
from .service import create_control, list_controls

router = APIRouter(prefix="/api/controls", tags=["Controls"])


@router.post("")
async def create_control_route(payload: CreateControlRequest):
    return await create_control(payload.dict())


@router.get("")
async def get_controls(frameworkId: str = Query(...)):
    return await list_controls(frameworkId)