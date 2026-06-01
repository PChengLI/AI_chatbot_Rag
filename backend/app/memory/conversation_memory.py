from sqlalchemy import select

from app.db.session import SessionLocal
from app.db.models import Message, Conversation


class ConversationMemory:

    def __init__(self):
        self.max_history = 10

    # =========================
    # 确保 conversation 存在（关键修复）
    # =========================
    def ensure_conversation(self, db, conversation_id: int):

        if conversation_id is None:
            return

        conv = db.get(Conversation, conversation_id)

        if not conv:

            conv = Conversation(
                id=conversation_id
            )

            db.add(conv)
            db.commit()

    # =========================
    # 保存消息（已修复 FK 问题）
    # =========================
    def save_message(
        self,
        conversation_id: int,
        role: str,
        content: str
    ):

        with SessionLocal() as db:

            # ⭐ 核心修复点
            self.ensure_conversation(db, conversation_id)

            message = Message(
                conversation_id=conversation_id,
                role=role,
                content=content
            )

            db.add(message)
            db.commit()

    # =========================
    # 获取历史
    # =========================
    def get_history(
        self,
        conversation_id: int
    ):

        if conversation_id is None:
            return []

        with SessionLocal() as db:

            stmt = (
                select(Message)
                .where(Message.conversation_id == conversation_id)
                .order_by(Message.created_at.asc())
            )

            result = db.execute(stmt)
            messages = result.scalars().all()

            # sliding window
            messages = messages[-self.max_history:]

            return [
                {
                    "role": msg.role,
                    "content": msg.content
                }
                for msg in messages
            ]

    # =========================
    # 清空历史（修复 async bug）
    # =========================
    def clear_history(
        self,
        conversation_id: int
    ):

        with SessionLocal() as db:

            stmt = (
                select(Message)
                .where(Message.conversation_id == conversation_id)
            )

            result = db.execute(stmt)
            messages = result.scalars().all()

            for msg in messages:
                db.delete(msg)

            db.commit()