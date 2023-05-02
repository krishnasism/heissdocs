from pydantic import BaseModel


class DocumentProgressRequest(BaseModel):
    userEmail: str
    documentId: str
    documentName: str
    stage: str | None
    pagesParsed: int | None
    totalPages: int | None
