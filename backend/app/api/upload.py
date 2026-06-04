from fastapi import APIRouter, UploadFile, File, HTTPException
from app.rag.ingestion import ingest_file
import os
import uuid
import traceback

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

    ext = os.path.splitext(file.filename)[1].lower()

    if ext not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {ext}"
        )

    file_id = str(uuid.uuid4())

    save_path = os.path.join(
        UPLOAD_DIR,
        f"{file_id}_{file.filename}"
    )

    try:

        print(f"[UPLOAD] filename={file.filename}")
        print(f"[UPLOAD] save_path={save_path}")
        print(f"[UPLOAD] kb_name={kb_name}")

        # 读取文件
        content = file.file.read()

        if not content:
            raise HTTPException(
                status_code=400,
                detail="Uploaded file is empty"
            )

        print(f"[UPLOAD] file_size={len(content)} bytes")

        # 保存文件
        with open(save_path, "wb") as f:
            f.write(content)

        print("[UPLOAD] file saved successfully")

        # RAG入库
        result = ingest_file(
            file_path=save_path,
            kb_name=kb_name
        )

        print(f"[UPLOAD] ingest result={result}")

        return {
            "success": True,
            "file_id": file_id,
            "filename": file.filename,
            "chunks": result.get("chunks", 0),
            "kb_name": kb_name
        }

    except HTTPException:
        raise

    except Exception as e:

        print("\n========== UPLOAD ERROR ==========")
        print(str(e))
        traceback.print_exc()
        print("==================================\n")

        raise HTTPException(
            status_code=500,
            detail=f"Upload failed: {str(e)}"
        )