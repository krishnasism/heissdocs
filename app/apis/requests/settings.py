from pydantic import BaseModel
from typing import Optional

class Settings(BaseModel):
    userEmail: str
    awsAccessKey: str
    awsSecret: str
    awsRegion: str
    noSqlProvider: str
    documentTableName: str
    parsingApiKey: Optional[str]
    bucketsList: str