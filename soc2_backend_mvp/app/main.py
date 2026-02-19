from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .db import ping_db

from .routes.auth_routes import router as auth_router
from .routes.company_profile_routes import router as company_profile_router
from .routes.document_routes import router as document_router
from .routes.export_routes import router as export_router
from app.routes.policy_pack_routes import router as policy_pack_router


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