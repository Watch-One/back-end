from typing import Optional
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: Optional[str]
    name: str
    email: EmailStr
    password: str
    lang: str
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Johnny Depp",
                "email": "jhonny@deep.com",
                "password": "strongpassword",
                "lang": "es"
            }
        }