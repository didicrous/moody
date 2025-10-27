from abc import ABC, abstractmethod
from .types import LLMRequest, LLMResponse

class LLMProvider(ABC):
    @abstractmethod
    def generate(self, req: LLMRequest) -> LLMResponse:
        ...
