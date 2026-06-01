from fastapi import APIRouter, HTTPException
from datetime import timedelta
from app.schemas.user import LoginRequest
from app.core.security import (
    verify_password,
    create_access_token
)

router = APIRouter()

FAKE_USER = {
    "username": "admin",
    "password": "123456"
}


@router.post("/login")
def login(req: LoginRequest):

    if req.username != FAKE_USER["username"]:
        raise HTTPException(
            status_code=401,
            detail="Invalid username"
        )

    if req.password != FAKE_USER["password"]:
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    token = create_access_token(
        data={"sub": req.username},
        expires_delta=timedelta(hours=12)
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }