"""Pydantic models for User entity."""

from pydantic import BaseModel, Field, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    full_name: str = Field(..., example="John Doe")

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool = True

    class Config:
        orm_mode = True
