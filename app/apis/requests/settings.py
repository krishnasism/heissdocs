from pydantic import BaseModel


class Settings(BaseModel):
    key: str
