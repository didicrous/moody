# backend/main.py
from fastapi import FastAPI
from backend.db import Base, engine
from backend.routers import auth

app = FastAPI(title="Moody API")

# Dev-only table creation (switch to Alembic later)
Base.metadata.create_all(bind=engine)

# Mount routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/healthz")
def healthz():
    return {"ok": True}