class QueryRouter:

    RAG_THRESHOLD = 0.3

    @classmethod
    def should_use_rag(
        cls,
        docs
    ):

        if not docs:
            return False

        score = docs[0].get(
            "rerank_score",
            0
        )

        return score >= cls.RAG_THRESHOLD
    
