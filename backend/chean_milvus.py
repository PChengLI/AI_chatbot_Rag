from pymilvus import utility, connections
from app.core.config import settings


connections.connect(
    host=settings.MILVUS_HOST,
    port=settings.MILVUS_PORT
)

collection_name = settings.MILVUS_COLLECTION

if utility.has_collection(collection_name):
    utility.drop_collection(collection_name)
    print(f"✅ Dropped collection: {collection_name}")
else:
    print("⚠️ Collection not found")