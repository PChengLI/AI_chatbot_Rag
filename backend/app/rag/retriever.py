from app.rag.embedding import (
    EmbeddingModel
)

from app.rag.milvus_client import (
    milvus_client
)


class DenseRetriever:
    def retrieve(
            self,
            query: str,
            kb_name: str = "default",
            top_k: int = 5
    ):

        query_embedding = (
            EmbeddingModel.embed_query(query)
        )

        docs = milvus_client.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        return docs