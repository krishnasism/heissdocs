from pydantic import BaseModel


class Settings(BaseModel):
    userEmail: str
    awsAccessKey: str
    awsSecret: str
    awsRegion: str
    noSqlProvider: str
    documentTableName: str
    parsingApiKey: str
    bucketsList: str