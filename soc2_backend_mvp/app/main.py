from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .db import ping_db

from .routes.auth_routes import router as auth_router
from .routes.company_profile_routes import router as company_profile_router
from .routes.document_routes import router as document_router
from .routes.export_routes import router as export_router
from app.routes.policy_pack_routes import router as policy_pack_router
from app.modules.company.routes import router as company_router
from app.modules.framework.routes import router as framework_router
from app.modules.control.routes import router as control_router
from app.modules.company_controls.routes import router as company_control_router
from app.modules.company_framework.routes import router as company_framework_router
from app.modules.board_configuration.routes import router as board_config_router

app = FastAPI(title=settings.API_NAME, version=settings.API_VERSION)

origins = [x.strip() for x in settings.CORS_ORIGINS.split(",") if x.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await ping_db()

@app.get("/api/health")
async def health():
    return {"ok": True, "name": settings.API_NAME, "version": settings.API_VERSION}

app.include_router(auth_router)
app.include_router(company_profile_router)
app.include_router(document_router)
app.include_router(export_router)
app.include_router(policy_pack_router)
app.include_router(company_router)
app.include_router(framework_router)
app.include_router(control_router)
app.include_router(company_control_router)
app.include_router(company_framework_router)
app.include_router(board_config_router)