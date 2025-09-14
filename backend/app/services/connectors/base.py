from abc import ABC, abstractmethod
from typing import Dict

class BaseConnector(ABC):
    @abstractmethod
    def test(self, config: Dict) -> bool:
        raise NotImplementedError
