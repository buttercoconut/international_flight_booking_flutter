"""Pydantic model for User.
"""

from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    email: EmailStr = Field(..., example="user@example.com")
    full_name: str = Field(..., example="John Doe")

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserRead(UserBase):
    id: int
