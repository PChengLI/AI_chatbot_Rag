from app.rag.milvus_client import milvus_client
from app.rag.bm25_retriever import BM25Retriever
from app.services.embedding_service import embedding_service


class HybridRetriever:

    def __init__(self):
        self.bm25 = BM25Retriever()

    def retrieve(
        self,
        query: str,
        kb_name: str = "default",
        top_k: int = 5
    ):

        # 1. embedding
        query_embedding = embedding_service.embed(query)

        # 2. vector retrieval
        vector_docs = milvus_client.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        # ❗ 关键：统一字段，去掉 Milvus 原始 score
        for doc in vector_docs:
            doc["vector_score"] = doc.pop("score", 0.0)

        # 3. BM25 retrieval
        self.bm25.add_documents(vector_docs)

        bm25_docs = self.bm25.search(
            query=query,
            top_k=top_k
        )

        # 4. fusion
        merged_docs = self.fuse_results(
            vector_docs,
            bm25_docs
        )

        return merged_docs

    def fuse_results(self, vector_docs, bm25_docs):

        merged = {}

        # vector results
        for rank, doc in enumerate(vector_docs):

            key = doc["content"]

            merged[key] = doc.copy()

            merged[key]["bm25_score"] = 0.0

            merged[key]["rrf_score"] = 1 / (rank + 60)

        # bm25 results
        for rank, doc in enumerate(bm25_docs):

            key = doc["content"]

            if key not in merged:

                merged[key] = doc.copy()

                merged[key]["vector_score"] = 0.0

                merged[key]["rrf_score"] = 0.0

            merged[key]["bm25_score"] = doc.get("bm25_score", 0.0)

            merged[key]["rrf_score"] += 1 / (rank + 60)

        results = list(merged.values())

        results.sort(
            key=lambda x: x["rrf_score"],
            reverse=True
        )

        return results