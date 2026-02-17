from fastapi import APIRouter

from ..models.user_model import UserCreate, UserLogin
from ..services.auth_service import register_user, login_user

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/register")
async def register(payload: UserCreate):
    return await register_user(payload.email, payload.password)


@router.post("/login")
async def login(payload: UserLogin):
    return await login_user(payload.email, payload.password)
