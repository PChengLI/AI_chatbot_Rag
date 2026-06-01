from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.chat import router as chat_router
from app.api.upload import router as upload_router
from app.api.kb import router as kb_router
from app.api.auth import router as auth_router
from app.api.health import router as health_router

from app.core.config import settings

import sys
import numpy

print("PYTHON PATH:", sys.executable)
print("NUMPY VERSION:", numpy.__version__)
from app.services.embedding_service import embedding_service



app = FastAPI(

    title=settings.APP_NAME,

    version="1.0.0",

    docs_url="/docs",

    redoc_url="/redoc"
)

# =========================
# CORS
# =========================

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)

# =========================
# Routers
# =========================

app.include_router(
    chat_router,
    prefix="/api/chat",
    tags=["Chat"]
)

app.include_router(
    upload_router,
    prefix="/api/upload",
    tags=["Upload"]
)

app.include_router(
    kb_router,
    prefix="/api/kb",
    tags=["Knowledge Base"]
)

app.include_router(
    auth_router,
    prefix="/api/auth",
    tags=["Auth"]
)

app.include_router(
    health_router,
    prefix="/api/health",
    tags=["Health"]
)


@app.get("/")
def root():

    return {
        "message": (
            "Enterprise RAG Chatbot Running"
        )
    }

print("🔥 App startup completed")