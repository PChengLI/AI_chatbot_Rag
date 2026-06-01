from pydantic import BaseModel
from typing import Optional


class KBCreate(BaseModel):

    name: str

    description: Optional[str] = None


class KBResponse(BaseModel):

    id: int

    name: str

    description: Optional[str]

    class Config:

        from_attributes = True