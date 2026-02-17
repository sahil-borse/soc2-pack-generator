from datetime import datetime, timezone
from bson import ObjectId

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt

from ..config import settings
from ..db import get_db
from ..utils.errors import unauthorized, not_found

security = HTTPBearer()


def _decode_token(token: str) -> str:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        user_id = payload.get("sub")
        if not user_id:
            unauthorized()
        return user_id
    except Exception:
        unauthorized()


def get_current_user_id(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    return _decode_token(credentials.credentials)


async def list_documents(user_id: str):
    db = get_db()
    cursor = db.documents.find({"userId": user_id}).sort("createdAt", -1)

    out = []
    async for doc in cursor:
        out.append({
            "id": str(doc["_id"]),
            "policyKey": doc["policyKey"],
            "title": doc["title"],
            "contentMarkdown": doc["contentMarkdown"],
            "createdAt": doc["createdAt"],
            "updatedAt": doc["updatedAt"],
        })

    return out


async def get_document(user_id: str, doc_id: str):
    db = get_db()
    doc = await db.documents.find_one({"_id": ObjectId(doc_id), "userId": user_id})
    if not doc:
        not_found("Document not found")

    return {
        "id": str(doc["_id"]),
        "policyKey": doc["policyKey"],
        "title": doc["title"],
        "contentMarkdown": doc["contentMarkdown"],
        "createdAt": doc["createdAt"],
        "updatedAt": doc["updatedAt"],
    }


async def update_document(user_id: str, doc_id: str, content_markdown: str):
    db = get_db()
    now = datetime.now(timezone.utc)

    res = await db.documents.update_one(
        {"_id": ObjectId(doc_id), "userId": user_id},
        {"$set": {"contentMarkdown": content_markdown, "updatedAt": now}},
    )

    if res.matched_count == 0:
        not_found("Document not found")

    return await get_document(user_id, doc_id)
