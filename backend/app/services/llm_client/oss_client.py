from typing import List

from sentence_transformers import SentenceTransformer

from .base import BaseLLMClient

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

class OSSClient(BaseLLMClient):
    def chat(self, messages: List[dict]) -> str:
        return "".join(m["content"] for m in messages)

    def embed(self, texts: List[str]) -> List[List[float]]:
        return model.encode(texts).tolist()
