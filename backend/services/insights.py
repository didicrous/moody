from pathlib import Path
from typing import Dict, Any
from backend.llm.types import LLMRequest
from backend.llm.providers.mock import MockProvider  # swap via DI later

PROMPT_PATH = Path(__file__).resolve().parents[1] / "llm" / "prompts" / "weekly_summary.txt"

def render_prompt(features: Dict[str, Any]) -> str:
    template = PROMPT_PATH.read_text()
    # Keep PII out: only derived stats, no free text notes
    lines = [template, "", "Features:"]
    for k, v in features.items():
        lines.append(f"- {k}: {v}")
    return "\n".join(lines)

def generate_weekly_summary(features: Dict[str, Any]) -> str:
    provider = MockProvider()  # later: inject real provider based on env
    prompt = render_prompt(features)
    res = provider.generate(LLMRequest(prompt=prompt, params={"temperature": 0.2}))
    return res.text
