from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    DateTime
)

from datetime import datetime


class Base(DeclarativeBase):
    pass


# =========================
# User
# =========================

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    username = Column(
        String(100),
        unique=True,
        nullable=False
    )

    hashed_password = Column(
        String(255),
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    conversations = relationship(
        "Conversation",
        back_populates="user"
    )


# =========================
# Conversation
# =========================

class Conversation(Base):

    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True)

    title = Column(String(255))

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="conversations"
    )

    messages = relationship(
        "Message",
        back_populates="conversation",
        cascade="all, delete-orphan"
    )


# =========================
# Message
# =========================

class Message(Base):

    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)

    conversation_id = Column(
        Integer,
        ForeignKey("conversations.id")
    )

    role = Column(String(50))

    content = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    conversation = relationship(
        "Conversation",
        back_populates="messages"
    )


# =========================
# Knowledge Base
# =========================

class KnowledgeBase(Base):

    __tablename__ = "knowledge_bases"

    id = Column(Integer, primary_key=True)

    name = Column(
        String(255),
        unique=True,
        nullable=False
    )

    description = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    documents = relationship(
        "Document",
        back_populates="kb",
        cascade="all, delete-orphan"
    )


# =========================
# Document
# =========================

class Document(Base):

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)

    kb_id = Column(
        Integer,
        ForeignKey("knowledge_bases.id")
    )

    filename = Column(String(255))

    file_path = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    kb = relationship(
        "KnowledgeBase",
        back_populates="documents"
    )