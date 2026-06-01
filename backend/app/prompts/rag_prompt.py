from app.prompts.system_prompt import SYSTEM_PROMPT

def format_history(history):

    if not history:
        return ""

    history_text = []

    for message in history:

        role = message["role"]

        content = message["content"]

        history_text.append(
            f"{role.upper()}: {content}"
        )

    return "\n".join(history_text)


# app/prompts/rag_prompt.py

from langchain_core.prompts import ChatPromptTemplate


rag_prompt = ChatPromptTemplate.from_template(
"""
You are a helpful AI assistant.

Conversation History:
{history}

Knowledge Context:
{context}

Question:
{question}

Answer:
"""
)