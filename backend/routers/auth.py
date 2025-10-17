import logging
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.db import get_db
from backend.models.user import User

router = APIRouter()
pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: str
    email: EmailStr
    created_at: str

@router.post("/register", response_model=UserOut, status_code=201)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    
    if db.scalar(select(User).where(User.email == data.email)):
        raise HTTPException(status_code=409, detail="Email already registered")
    logging.info("Unique email")
    user = User(email=data.email, hashed_password=pwd.hash(data.password))
    logging.info("before user commit")
    # commit entry, refresh to keep current
    db.add(user); db.commit(); db.refresh(user)
    logging.info("after user commit")    
    return UserOut(id=str(user.id), email=user.email, created_at=str(user.created_at))
