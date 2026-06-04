import os

from langchain.text_splitter import (
    RecursiveCharacterTextSplitter
)

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredWordDocumentLoader
)

from app.rag.embedding import EmbeddingModel
from app.rag.milvus_client import milvus_client


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)


def load_documents(file_path: str):

    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":

        loader = PyPDFLoader(file_path)

    elif ext == ".docx":

        loader = UnstructuredWordDocumentLoader(
            file_path
        )

    elif ext in [".txt", ".md"]:

        loader = TextLoader(
            file_path=file_path,
            encoding="utf-8",
            autodetect_encoding=True
        )

    else:

        raise ValueError(
            f"Unsupported file type: {ext}"
        )

    return loader.load()


def ingest_file(file_path: str, kb_name: str = "default"):

    documents = load_documents(file_path)

    chunks = text_splitter.split_documents(documents)

    texts = [
        doc.page_content
        for doc in chunks
        if doc.page_content.strip()
    ]

    if not texts:
        raise ValueError("No valid text extracted from document")

    embeddings = EmbeddingModel.embed_documents(texts)

    vectors = []
    payloads = []

    for doc, embedding in zip(chunks, embeddings):

        vectors.append(embedding)

        payloads.append({
            "text": doc.page_content,   # ⚠️ 必须叫 text（你的 MilvusClient 用的）
            "source": file_path,
            "kb_name": kb_name
        })

    milvus_client.insert(
        vectors=vectors,
        payloads=payloads
    )

    return {
        "success": True,
        "chunks": len(vectors),
        "filename": os.path.basename(file_path)
    }