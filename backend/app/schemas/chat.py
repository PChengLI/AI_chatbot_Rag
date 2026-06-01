from pydantic import BaseModel
from typing import Optional
from typing import List

class ChatRequest(BaseModel):

    query: str

    kb_name: Optional[str] = None
    conversation_id: Optional[int] = None
    
    session_id: Optional[str] = None
    top_k: int = 5
class SourceDocument(BaseModel):

    source: str

    content: str

    score: float


class ChatResponse(BaseModel):

    answer: str

    conversation_id: int

    sources: List[SourceDocument]