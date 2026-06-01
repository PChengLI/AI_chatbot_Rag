from fastapi import APIRouter, UploadFile, File, HTTPException
from app.rag.ingestion import ingest_file
import os
import uuid

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/")
def upload_document(
    file: UploadFile = File(...),
    kb_name: str = "default"
):

    allowed_types = [
        ".pdf",
        ".txt",
        ".docx",
        ".md"
    ]

    ext = os.path.splitext(file.filename)[1]

    if ext not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type"
        )

    file_id = str(uuid.uuid4())

    save_path = os.path.join(
        UPLOAD_DIR,
        f"{file_id}_{file.filename}"
    )



    with open(save_path, "wb") as f:
        print(len(file.read()))
        f.write(file.read())

    result = ingest_file(
        file_path=save_path,
        kb_name=kb_name
    )

    return {
        "success": True,
        "file_id": file_id,
        "filename": file.filename,
        "chunks": result["chunks"],
        "kb_name": kb_name
    }