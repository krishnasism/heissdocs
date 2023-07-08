from pydantic import BaseModel
from typing import Optional


class Settings(BaseModel):
    userEmail: str
    awsAccessKey: Optional[str]
    awsSecret: Optional[str]
    awsRegion: Optional[str]
    noSqlProvider: Optional[str]
    documentTableName: Optional[str]
    parsingApiKey: Optional[str]
    bucketsList: Optional[str]
    scanBucket: Optional[str]
    elasticSearchHost: Optional[str]
    elasticSearchPort: Optional[int]
    elasticSearchApiKey: Optional[str]
