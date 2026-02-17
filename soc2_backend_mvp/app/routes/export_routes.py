from fastapi import APIRouter, Depends
from fastapi.responses import Response

from ..services.document_service import get_current_user_id
from ..services.export_service import export_docx_single, export_docx_pack_zip

router = APIRouter(prefix="/api/export", tags=["export"])


@router.get("/documents/{doc_id}/docx")
async def download_doc(doc_id: str, user_id: str = Depends(get_current_user_id)):
    data, title = await export_docx_single(user_id, doc_id)
    safe = title.replace(" ", "_")
    return Response(
        content=data,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={"Content-Disposition": f"attachment; filename={safe}.docx"},
    )


@router.get("/pack/docx")
async def download_pack(user_id: str = Depends(get_current_user_id)):
    data = await export_docx_pack_zip(user_id)
    return Response(
        content=data,
        media_type="application/zip",
        headers={"Content-Disposition": "attachment; filename=soc2_policy_pack.zip"},
    )
