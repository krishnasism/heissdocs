from pydantic import BaseModel

class AuthRequest(BaseModel):
    userEmail: str
    userKey: str
