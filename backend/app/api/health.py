from fastapi import APIRouter
from datetime import datetime

router = APIRouter()


@router.get("/")
def health():

    return {
        "status": "healthy",
        "service": "enterprise-rag-chatbot",
        "timestamp": datetime.utcnow().isoformat()
    }