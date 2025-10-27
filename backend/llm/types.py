from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class LLMRequest:
    prompt: str
    params: Dict[str, Any] = None  # e.g., temperature, max_tokens

@dataclass
class LLMResponse:
    text: str
    usage: Dict[str, Any] | None = None
