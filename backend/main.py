from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.db import Base, engine, get_db
from backend.models.user import User

app = FastAPI()
# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

Base.metadata.create_all(bind=engine)

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: str
    email: EmailStr
    created_at: str

@app.post("/auth/register", response_model=UserOut, status_code=201)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    existing = db.scalar(select(User).where(User.email == data.email))
    if existing:
        raise HTTPException(status_code=409, detail="Email already registered")

    hashed_pw = pwd_context.hash(data.password)
    user = User(email=data.email, hashed_password=hashed_pw)
    db.add(user)
    db.commit()
    db.refresh(user)
    return UserOut(id=str(user.id), email=user.email, created_at=str(user.created_at))

@app.get("/healthz")
def healthz():
    return {"ok": True}
