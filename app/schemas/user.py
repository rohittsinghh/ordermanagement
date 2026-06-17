from pydantic import BaseModel, EmailStr
from typing import Literal, Optional


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    phone: str
    role: Literal["admin", "user"]


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    role: Optional[Literal["admin", "user"]] = None


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    phone: str
    role: str