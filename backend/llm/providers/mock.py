from .base import LLMProvider
from ..types import LLMRequest, LLMResponse

class MockProvider(LLMProvider):
    def generate(self, req: LLMRequest) -> LLMResponse:
        return LLMResponse(text="This week, consistent sleep correlated with improved mood. (mock)")
