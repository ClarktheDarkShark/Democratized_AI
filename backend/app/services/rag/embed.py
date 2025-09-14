from typing import List

from ..llm_client.base import BaseLLMClient


def embed_texts(client: BaseLLMClient, texts: List[str]) -> List[List[float]]:
    return client.embed(texts)
