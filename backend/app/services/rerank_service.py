from app.rag.rerank import (
    BGEReranker
)


class RerankService:

    def __init__(self):

        self.reranker = (
            BGEReranker()
        )

    def rerank(
        self,
        query: str,
        docs: list
    ):

        return self.reranker.rerank(
            query=query,
            docs=docs
        )


rerank_service = RerankService()