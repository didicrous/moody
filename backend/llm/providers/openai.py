import os
from .base import LLMProvider
from ..types import LLMRequest, LLMResponse

class OpenAIProvider(LLMProvider):
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise RuntimeError("OPENAI_API_KEY not set")

    def generate(self, req: LLMRequest) -> LLMResponse:
        # Pseudocode only; keep real SDK calls out until ready
        # resp = openai.chat.completions.create(model="gpt-4o-mini", messages=[...], ...)
        # return LLMResponse(text=resp.choices[0].message.content, usage=resp.usage)
        raise NotImplementedError("Wire provider when ready")
