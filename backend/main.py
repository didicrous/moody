from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext

app = FastAPI()

# Password hashing 
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str

@app.post("/auth/register")
def register(data: RegisterRequest):
    hashed_pw = pwd_context.hash(data.password)
    return {"email": data.email, "hashed_password": hashed_pw}