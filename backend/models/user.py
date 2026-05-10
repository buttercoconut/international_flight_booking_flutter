# models/user.py
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    user_id: str
    email: EmailStr
    full_name: str
    phone: str
    # password hash would be stored securely
