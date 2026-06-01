from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # =====================
    # App
    # =====================
    APP_NAME: str = "Enterprise RAG Chatbot"
    ENV: str = "dev"
    DEBUG: bool = True

    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # =====================
    # LLM
    # =====================
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-5.4-mini"
    BASE_URL: str = "https://api.zhizengzeng.com/v1"

    # =====================
    # Embedding / Rerank
    # =====================
    EMBEDDING_MODEL_NAME: str = "BAAI/bge-large-en-v1.5"
    RERANK_MODEL_NAME: str = "BAAI/bge-reranker-base"

    # =====================
    # Milvus
    # =====================
    MILVUS_HOST: str = "localhost"
    MILVUS_PORT: int = 19530
    MILVUS_COLLECTION: str = "enterprise_rag"

    # =====================
    # PostgreSQL
    # =====================
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "rag_chatbot"
    DATABASE_URL: str
    # =====================
    # JWT
    # =====================
    JWT_SECRET_KEY: str = "change_me"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 1440

    # =====================
    # Pydantic config
    # =====================
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()