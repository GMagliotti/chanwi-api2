from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCredentials(BaseModel):
    email: EmailStr
    password: str
    role: str