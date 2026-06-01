from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.schemas.chat import ChatRequest
from app.chains.rag_chain import RAGChain
import traceback
router = APIRouter()
rag_chain = RAGChain()

@router.post("/")
def chat(req: ChatRequest):

    try:
        result = rag_chain.chat(
            query=req.query,
            conversation_id=req.conversation_id,
            kb_name=req.kb_name,
            top_k=req.top_k
        )

        return {
            "success": True,
            "answer": result["answer"],
            "sources": result["sources"],
            "retrieved_docs": result["retrieved_docs"]
        }

    except Exception as e:
        traceback.print_exc()
        return {
            "error": str(e)
        }
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/stream")
def stream_chat(req: ChatRequest):

    def event_generator():

        for chunk in rag_chain.stream_chat(
            query=req.query,
            conversation_id=req.conversation_id,
            kb_name=req.kb_name
        ):
            yield f"data: {chunk}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )

@router.post("/")
def chat(request: ChatRequest):

    try:

        answer = rag_chain.chat(
            query=request.query
        )

        return {
            "answer": answer
        }

    except Exception as e:

        traceback.print_exc()

        return {
            "error": str(e)
        }