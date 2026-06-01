from sqlalchemy.ext.asyncio import (
    create_async_engine
)

from app.core.config import settings


DATABASE_URL = (

    f"postgresql+asyncpg://"

    f"{settings.POSTGRES_USER}:"

    f"{settings.POSTGRES_PASSWORD}@"

    f"{settings.POSTGRES_HOST}:"

    f"{settings.POSTGRES_PORT}/"

    f"{settings.POSTGRES_DB}"
)

engine = create_async_engine(

    DATABASE_URL,

    echo=True
)