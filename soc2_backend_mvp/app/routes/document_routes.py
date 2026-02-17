from datetime import datetime, timezone

from fastapi import APIRouter, Depends
from bson import ObjectId

from ..db import get_db
from ..services.document_service import get_current_user_id, list_documents, get_document, update_document
from ..services.company_profile_service import get_company_profile
from ..ai.prompts import POLICIES
from ..ai.policy_generator import generate_policy_markdown
from ..models.document_model import DocumentUpdate

router = APIRouter(prefix="/api/documents", tags=["documents"])


@router.get("")
async def get_all_docs(user_id: str = Depends(get_current_user_id)):
    return await list_documents(user_id)


@router.get("/{doc_id}")
async def get_one_doc(doc_id: str, user_id: str = Depends(get_current_user_id)):
    return await get_document(user_id, doc_id)


@router.put("/{doc_id}")
async def update_one_doc(doc_id: str, payload: DocumentUpdate, user_id: str = Depends(get_current_user_id)):
    return await update_document(user_id, doc_id, payload.contentMarkdown)


@router.post("/generate-pack")
async def generate_pack(user_id: str = Depends(get_current_user_id)):
    db = get_db()

    profile_doc = await get_company_profile(user_id)
    company_profile = profile_doc.get("profile", {})

    now = datetime.now(timezone.utc)

    generated = []

    for p in POLICIES:
        md = await generate_policy_markdown(p["title"], company_profile)

        await db.documents.update_one(
            {"userId": user_id, "policyKey": p["key"]},
            {"$set": {
                "userId": user_id,
                "policyKey": p["key"],
                "title": p["title"],
                "contentMarkdown": md,
                "updatedAt": now,
            }, "$setOnInsert": {"createdAt": now}},
            upsert=True,
        )

        generated.append({"policyKey": p["key"], "title": p["title"]})

    return {"message": "Generated SOC2 policy pack", "generated": generated}
