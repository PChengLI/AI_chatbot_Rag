from app.rag.hybrid_search import HybridRetriever
from app.rag.rerank import BGEReranker

from app.services.llm_service import llm_service
from app.memory.conversation_memory import ConversationMemory

from app.prompts.rag_prompt import rag_prompt

from app.router.query_router import QueryRouter


class RAGChain:

    def __init__(self):

        # ===== Retrieval Layer =====
        self.retriever = HybridRetriever()
        self.reranker = BGEReranker()

        # ===== LLM =====
        self.llm = llm_service

        # ===== Memory =====
        self.memory = ConversationMemory()

        # ===== LangChain RAG Chain =====
        self.chain = (
            rag_prompt
            | self.llm.llm
        )

    def chat(
        self,
        query: str,
        conversation_id: str = None,
        kb_name: str = "default",
        top_k: int = 5
    ):

        # =========================
        # 1. Load history
        # =========================
        history = self.memory.get_history(conversation_id)

        # =========================
        # 2. Retrieval (Hybrid)
        # =========================
        retrieved_docs = self.retriever.retrieve(
            query=query,
            kb_name=kb_name,
            top_k=top_k
        )

        # =========================
        # 3. Rerank
        # =========================
        reranked_docs = self.reranker.rerank(
            query=query,
            docs=retrieved_docs
        )

        # =========================
        # 4. Router (关键：决定是否走RAG)
        # =========================
        use_rag = QueryRouter.should_use_rag(reranked_docs)

        # =========================
        # 5. Chat Mode（不走知识库）
        # =========================
        if not use_rag:

            response = self.llm.llm.invoke(
                f"""
You are a helpful assistant.

Conversation history:
{history}

User question:
{query}

Answer naturally and concisely.
"""
            )

            answer = response.content

            self._save_memory(conversation_id, query, answer)

            return {
                "mode": "chat",
                "answer": answer,
                "sources": [],
                "retrieved_docs": []
            }

        # =========================
        # 6. RAG Mode（走知识库）
        # =========================

        context = self.build_context(reranked_docs)

        response = self.chain.invoke(
            {
                "question": query,
                "context": context,
                "history": history
            }
        )

        answer = response.content

        self._save_memory(conversation_id, query, answer)

        return {
            "mode": "rag",
            "answer": answer,
            "sources": [
                doc.get("source", "")
                for doc in reranked_docs
            ],
            "retrieved_docs": reranked_docs
        }

    def build_context(self, docs):

        context_parts = []

        for i, doc in enumerate(docs):

            context_parts.append(
                f"""Document {i + 1}
Source: {doc.get('source', '')}

Content:
{doc.get('content', '')}
"""
            )

        return "\n\n".join(context_parts)

    def _save_memory(self, conversation_id, query, answer):

        if not conversation_id:
            return

        self.memory.save_message(
            conversation_id=conversation_id,
            role="user",
            content=query
        )

        self.memory.save_message(
            conversation_id=conversation_id,
            role="assistant",
            content=answer
        )