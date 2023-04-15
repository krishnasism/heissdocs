from pydantic import BaseModel


class PDFUploadRequest(BaseModel):
    summarize: str
