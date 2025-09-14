from abc import ABC, abstractmethod
from typing import Dict

class BaseTool(ABC):
    name: str

    @abstractmethod
    def execute(self, args: Dict) -> Dict:
        raise NotImplementedError
