import asyncio

from app.db.postgres import engine
from app.db.models import Base


def init():

    with engine.begin() as conn:

        conn.run_sync(
            Base.metadata.create_all
        )

    print("Database tables created")


if __name__ == "__main__":

    asyncio.run(init())