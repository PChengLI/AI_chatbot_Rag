from sentence_transformers import (
    CrossEncoder
)

from app.core.config import settings


class BGEReranker:

    _model = None

    @classmethod
    def get_model(cls):

        if cls._model is None:

            cls._model = CrossEncoder(
                settings.RERANK_MODEL_NAME
            )

        return cls._model

    def rerank(
        self,
        query: str,
        docs: list
    ):

        if not docs:
            return docs

        model = self.get_model()

        pairs = [

            (query, doc["content"])

            for doc in docs
        ]

        scores = model.predict(pairs)

        for doc, score in zip(
            docs,
            scores
        ):

            doc["rerank_score"] = (
                float(score)
            )

        docs.sort(
            key=lambda x: x["rerank_score"],
            reverse=True
        )

        return docs