from app.rag.embedding import EmbeddingModel
from app.rag.milvus_client import milvus_client
import uuid


docs = [
    "Milvus is a vector database for similarity search.",
    "RAG combines retrieval and generation using LLMs.",
    "BGE is a strong embedding model from BAAI.",
    "LangChain is a framework for building LLM applications."
]


def ingest():

    vectors = []
    payloads = []

    for doc in docs:

        vec = EmbeddingModel.embed_documents(doc)

        vectors.append(vec)

        payloads.append({
            "id": str(uuid.uuid4()),
            "text": doc,
            "kb_name": "default"
        })

    milvus_client.insert(
        vectors=vectors,
        payloads=payloads
    )
    print(1)
    print("✅ ingestion done")


if __name__ == "__main__":
    ingest()