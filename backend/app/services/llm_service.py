# app/services/llm_service.py

from langchain_openai import ChatOpenAI
from app.core.config import settings


class LLMService:

    def __init__(self):

        self.llm = ChatOpenAI(
            model=settings.OPENAI_MODEL,
            api_key=settings.OPENAI_API_KEY,
            base_url=settings.BASE_URL,
            temperature=0.7
        )

    def generate(self, prompt):

        response = self.llm.invoke(prompt)

        return response.content


llm_service = LLMService()