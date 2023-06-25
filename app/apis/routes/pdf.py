from fastapi import APIRouter, UploadFile, Form, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer
from typing import Annotated
from services.search.search import get_pdf_by_query
from services.storage.storage_ops import get_presigned_url
from services.security.verify_token import verify_token
from services.queue.queue import prepare_job
from apis.requests.document_progress import DocumentProgressRequest
from enums.FileStages import FileStages
from services.local.postgres import PostgresManager

import logging

router = APIRouter()
token_auth_scheme = HTTPBearer()
pm = PostgresManager()


@router.get("/search")
async def pdf_search(
    query: str, user_email: str, authenticated: bool = Depends(verify_token)
):
    query = query.lower()
    documents = get_pdf_by_query(query, user_email)

    return JSONResponse(content={"documents": documents}, status_code=200)


@router.post("/upload")
async def upload_pdf(
    file: UploadFile,
    summarize: Annotated[str, Form()],
    user_email: Annotated[str, Form()],
    store_files_in_cloud: Annotated[bool, Form()],
    bucket_name: Annotated[str, Form()],
    authenticated: bool = Depends(verify_token),
):
    try:
        document_id = prepare_job(
            file,
            params={
                "summarize": summarize,
                "user_email": user_email,
                "store_files_in_cloud": store_files_in_cloud,
                "bucket_name": bucket_name,
            },
        )

        pm.create_documents_progress_entry(
            DocumentProgressRequest(
                userEmail=user_email,
                documentId=document_id,
                documentName=file.filename,
                stage=FileStages.QUEUED.value,
                pagesParsed=0,
                totalPages=0,
            ).dict()
        )

        return JSONResponse(content={"message": "Created"}, status_code=201)
    except Exception as e:
        logging.error(e)
        return JSONResponse(content={"error": str(e)}, status_code=500)


@router.get("/get-file-url")
async def get_file_url(
    bucket_name: str,
    file_name: str,
    user_email: str,
    authenticated: bool = Depends(verify_token),
):
    try:
        url = get_presigned_url(bucket_name, file_name, user_email)

        return JSONResponse(
            content={"success": "true", "file_url": url}, status_code=200
        )
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
