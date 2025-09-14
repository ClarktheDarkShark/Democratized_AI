from typing import List

from openai import OpenAI

from ...core.config import settings
from .base import BaseLLMClient

client = OpenAI(api_key=settings.llm_api_key)

class OpenAIClient(BaseLLMClient):
    def chat(self, messages: List[dict]) -> str:  # pragma: no cover
        completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
        return completion.choices[0].message["content"]

    def embed(self, texts: List[str]) -> List[List[float]]:  # pragma: no cover
        emb = client.embeddings.create(model="text-embedding-3-small", input=texts)
        return [e["embedding"] for e in emb.data]
