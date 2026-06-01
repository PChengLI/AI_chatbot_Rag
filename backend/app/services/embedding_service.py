from sentence_transformers import SentenceTransformer
from app.core.config import settings

class EmbeddingService:
    def __init__(self):
        self.model = SentenceTransformer(
            settings.EMBEDDING_MODEL_NAME
        )
    def embed(self, text: str):

        return self.model.encode(
            text,
            normalize_embeddings=True
        )

    def embed_batch(self, texts: list[str]):

        return self.model.encode(
            texts,
            normalize_embeddings=True
        )


embedding_service = EmbeddingService()