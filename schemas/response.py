from typing import Optional
from pydantic import BaseModel

class LoginResponseSchema(BaseModel):
    message: Optional[str]
    token: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "message": "Mensajito",
                "access_token": "Token generado"
            }
        }