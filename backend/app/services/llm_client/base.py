from abc import ABC, abstractmethod
from typing import List

class BaseLLMClient(ABC):
    @abstractmethod
    def chat(self, messages: List[dict]) -> str:
        raise NotImplementedError

    @abstractmethod
    def embed(self, texts: List[str]) -> List[List[float]]:
        raise NotImplementedError
