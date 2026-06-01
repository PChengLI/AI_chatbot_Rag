from langchain.text_splitter import (
    RecursiveCharacterTextSplitter
)

from app.rag.embedding import EmbeddingModel
from app.rag.milvus_client import milvus_client


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)


def ingest_file(
    file_path: str,
    kb_name: str = "default"
):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:

        text = f.read()

    chunks = text_splitter.split_text(text)

    embeddings = (
        EmbeddingModel.embed_documents(chunks)
    )

    docs = []

    for chunk, embedding in zip(
        chunks,
        embeddings
    ):

        docs.append({

            "content": chunk,

            "source": file_path,

            "embedding": embedding
        })

    milvus_client.insert(docs)

    return {
        "chunks": len(chunks)
    }