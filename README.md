🌿 **Journaling App (WIP)**

A simple mood-tracking and journaling app built with FastAPI.
Users will log moods, reflect on habits, and eventually receive AI-generated insights.

🚧 **Current progress**

* FastAPI setup complete

* /auth/register endpoint live

* Input validation (Pydantic) + password hashing (bcrypt)


⚙️ **Run locally** 
pip install fastapi uvicorn passlib[bcrypt] pydantic
uvicorn main:app --reload


Visit http://127.0.0.1:8000/docs
 → test POST /auth/register

