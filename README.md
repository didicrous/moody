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




⚙️ Backend

FastAPI — lightweight Python framework for rapid, async REST APIs

SQLAlchemy ORM — schema-first modeling, typed relationships, and database abstraction

SQLite → PostgreSQL — local dev persistence, scalable production migration path

Alembic (planned) — version-controlled migrations

Pydantic — input validation and serialization

bcrypt (Passlib) — secure password hashing

JWT Auth (upcoming) — token-based session management for mobile clients

🧱 Application Architecture

Modular route organization with APIRouter

Clean separation of models, db, and routers

Central SessionLocal dependency injection pattern for transactional safety

Layered service design to support future AI inference modules (LLM-based insight generation)

Ready for async expansion with background tasks and event streaming

🤖 AI & Data Pipeline (in design)

Embedding-based similarity models for mood correlation

Sentiment analysis on journal entries for behavioral insights

Planned vector database integration for efficient retrieval (FAISS or Qdrant)

Structured data pipeline for weekly mood summaries and personalized insights

📱 Frontend (planned)

React Native (Expo) — cross-platform mobile app

Recharts for mood visualization

JWT auth flow integrated via Axios API client

🧩 Dev Environment

.env for local configuration

.gitignore for clean repo hygiene (__pycache__, app.db, .venv)

Fully reproducible via requirements.txt

Visit http://127.0.0.1:8000/docs
 → test POST /auth/register


