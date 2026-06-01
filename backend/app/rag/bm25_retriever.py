from rank_bm25 import BM25Okapi


class BM25Retriever:

    def __init__(self):

        self.documents = []
        self.tokenized_docs = []

        self.bm25 = None

    def add_documents(self, docs):

        self.documents = docs

        self.tokenized_docs = [
            doc["content"].lower().split()
            for doc in docs
        ]

        self.bm25 = BM25Okapi(
            self.tokenized_docs
        )

    def search(
        self,
        query: str,
        top_k: int = 5
    ):

        if not self.bm25:
            return []

        tokenized_query = (
            query.lower().split()
        )

        scores = self.bm25.get_scores(
            tokenized_query
        )

        scored_docs = []

        for idx, score in enumerate(scores):

            doc = self.documents[idx].copy()

            doc["bm25_score"] = float(score)

            scored_docs.append(doc)

        scored_docs.sort(
            key=lambda x: x["bm25_score"],
            reverse=True
        )

        return scored_docs[:top_k]