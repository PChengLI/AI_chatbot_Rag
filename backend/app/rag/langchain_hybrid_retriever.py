from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever

from app.rag.hybrid_search import HybridRetriever


class LangChainHybridRetriever(
    BaseRetriever
):

    def __init__(
        self,
        top_k: int = 5
    ):

        super().__init__()

        self.top_k = top_k

        self.hybrid = HybridRetriever()

    def _get_relevant_documents(
        self,
        query: str
    ):

        docs = self.hybrid.retrieve(
            query=query,
            top_k=self.top_k
        )

        return [

            Document(
                page_content=doc["content"],
                metadata={
                    "source": doc.get(
                        "source",
                        ""
                    ),
                    "score": doc.get(
                        "rerank_score",
                        0
                    )
                }
            )

            for doc in docs
        ]