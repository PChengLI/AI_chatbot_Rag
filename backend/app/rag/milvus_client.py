from pymilvus import (
    connections,
    Collection,
    CollectionSchema,
    FieldSchema,
    DataType,
    utility
)

from app.core.config import settings


class MilvusClient:

    def __init__(self):

        connections.connect(
            alias="default",
            host=settings.MILVUS_HOST,
            port=settings.MILVUS_PORT
        )

        self.collection_name = settings.MILVUS_COLLECTION

        self.collection = self._init_collection()

    def _init_collection(self):

        if utility.has_collection(self.collection_name):
            collection = Collection(self.collection_name)
            collection.load()
            return collection

        fields = [

            FieldSchema(
                name="id",
                dtype=DataType.INT64,
                is_primary=True,
                auto_id=True
            ),

            FieldSchema(
                name="content",
                dtype=DataType.VARCHAR,
                max_length=65535
            ),

            FieldSchema(
                name="source",
                dtype=DataType.VARCHAR,
                max_length=500
            ),

            FieldSchema(
                name="kb_name",
                dtype=DataType.VARCHAR,
                max_length=100
            ),

            FieldSchema(
                name="embedding",
                dtype=DataType.FLOAT_VECTOR,
                dim=1024
            )
        ]

        schema = CollectionSchema(
            fields,
            description="RAG collection with kb support"
        )

        collection = Collection(
            name=self.collection_name,
            schema=schema
        )

        collection.create_index(
            field_name="embedding",
            index_params={
                "metric_type": "COSINE",
                "index_type": "IVF_FLAT",
                "params": {"nlist": 128}
            }
        )

        collection.load()

        return collection

    # ------------------------
    # INSERT（已修复）
    # ------------------------
    def insert(self, vectors, payloads):

        contents = [p["text"] for p in payloads]
        sources = [p.get("source", "") for p in payloads]
        kb_names = [p.get("kb_name", "default") for p in payloads]

        data = [
            contents,
            sources,
            kb_names,
            vectors
        ]

        self.collection.insert(data)
        self.collection.flush()

    # ------------------------
    # SEARCH（已升级支持 kb filter）
    # ------------------------
    def search(self, query_embedding: list, top_k: int = 5, kb_name: str = None):

        expr = None

        if kb_name:
            expr = f'kb_name == "{kb_name}"'

        results = self.collection.search(
            data=[query_embedding],
            anns_field="embedding",
            param={
                "metric_type": "COSINE",
                "params": {"nprobe": 10}
            },
            limit=top_k,
            expr=expr,
            output_fields=[
                "content",
                "source",
                "kb_name"
            ]
        )

        docs = []

        for hits in results:

            for hit in hits:

                docs.append({
                    "content": hit.entity.get("content"),
                    "source": hit.entity.get("source"),
                    "kb_name": hit.entity.get("kb_name"),
                    "score": float(hit.score)
                })

        return docs


milvus_client = MilvusClient()