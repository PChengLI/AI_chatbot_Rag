from fastapi import APIRouter, HTTPException
from app.services.kb_service import KBService
from app.schemas.kb import KBCreate

router = APIRouter()

kb_service = KBService()


@router.get("/")
async def list_kbs():

    return await kb_service.list_kbs()


@router.post("/")
def create_kb(req: KBCreate):

    result = kb_service.create_kb(
        name=req.name,
        description=req.description
    )

    return {
        "success": True,
        "kb": result
    }


@router.delete("/{kb_name}")
def delete_kb(kb_name: str):

    deleted = kb_service.delete_kb(kb_name)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Knowledge base not found"
        )

    return {
        "success": True
    }