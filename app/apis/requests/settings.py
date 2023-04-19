from pydantic import BaseModel


class Settings(BaseModel):
    awsAccessKey: str
    awsSecret: str
    awsRegion: str
    noSqlProvider: str
    documentTableName: str
    parsingApiKey: str
