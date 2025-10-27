🌿 **Journaling App (WIP)**

A simple mood-tracking and journaling app built with FastAPI.
Users will log moods, reflect on habits, and eventually receive AI-generated insights.

🚧 **Current progress**

* FastAPI setup complete

* /auth/register endpoint live

* Input validation (Pydantic) + password hashing (bcrypt)

### 🧠 LLM Orchestration (scaffolded)
- Adapter pattern (`llm/providers`) decouples model vendors from app logic
- Prompt templates in `llm/prompts` with version control
- Privacy by design: prompts accept **derived features only** (no raw notes/PII)
- Mock provider for tests/dev; real provider injected via env at deploy time

⚙️ **Run locally** 
pip install fastapi uvicorn passlib[bcrypt] pydantic
uvicorn main:app --reload




Visit http://127.0.0.1:8000/docs
 → test POST /auth/register

