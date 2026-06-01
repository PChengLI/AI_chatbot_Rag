import os

from app.rag.ingestion import (
    ingest_file
)

from app.db.models import (
    KnowledgeBase
)

from app.db.session import (
    SessionLocal
)


class KBService:

    def create_kb(
        self,
        name: str,
        description: str = ""
    ):

        with SessionLocal() as db:

            kb = KnowledgeBase(
                name=name,
                description=description
            )

            db.add(kb)

            db.commit()

            db.refresh(kb)

            return kb

    def ingest_document(
        self,
        file_path: str
    ):

        result = ingest_file(
            file_path=file_path
        )

        return result


kb_service = KBService()