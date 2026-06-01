from sentence_transformers import SentenceTransformer
from app.core.config import settings
import numpy as np


class EmbeddingModel:

    _model = None

    @classmethod
    def get_model(cls):

        if cls._model is None:

            cls._model = SentenceTransformer(
                settings.EMBEDDING_MODEL_NAME
            )

        return cls._model

    @classmethod
    def embed_query(
        cls,
        text: str
    ):

        model = cls.get_model()

        embedding = model.encode(
            text,
            normalize_embeddings=True
        )

        return embedding.tolist()

    @classmethod
    def embed_documents(
        cls,
        documents: list[str]
    ):

        model = cls.get_model()

        embeddings = model.encode(
            documents,
            normalize_embeddings=True,
            batch_size=32,
            show_progress_bar=False
        )

        return embeddings.tolist()