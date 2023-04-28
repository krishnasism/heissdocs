from fastapi import APIRouter, UploadFile, Form, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer
from typing import Annotated
from services.pdf.parsing.parser import get_pdf_body
from services.search.search import get_pdf_by_query
from services.summarize.summary import summarize_text
from services.storage.storage_ops import process_s3_files, get_presigned_url
from services.security.verify_token import verify_token
from app.services.queue.rabbit import send_queue_message

router = APIRouter()
token_auth_scheme = HTTPBearer()


@router.get("/search")
async def pdf_search(query: str, authenticated: bool = Depends(verify_token)):
    query = query.lower()
    documents = get_pdf_by_query(query)

    return JSONResponse(
        content={
            "documents": documents
        },
        status_code=200
    )


@ router.post("/upload")
async def upload_pdf(file: UploadFile, summarize: Annotated[str, Form()], user_email: Annotated[str, Form()], store_files_in_cloud: Annotated[bool, Form()], bucket_name: Annotated[str, Form()], authenticated: bool = Depends(verify_token)):
    try:
        pdf_body = get_pdf_body(file, store_files_in_cloud, bucket_name)
        if summarize == "true":
            # TODO: Doesn't work as expected - keep False for now
            # pdf_body = summarize_text(pdf_body)
            pass

        return JSONResponse(
            content={
                "parse_result": {
                    "pdf_body": pdf_body
                }
            },
            status_code=200
        )
    except Exception as e:
        return JSONResponse(
            content={
                "error": str(e)
            },
            status_code=500
        )


@ router.post("/process-s3-bucket")
async def process_s3_bucket(bucket_name: str, authenticated: bool = Depends(verify_token)):
    try:
        process_s3_files(bucket_name)

        return JSONResponse(
            content={
                "success": "true"
            },
            status_code=200
        )
    except Exception as e:
        return JSONResponse(
            content={
                "error": str(e)
            },
            status_code=500
        )


@ router.get("/get-file-url")
async def get_file_url(bucket_name: str, file_name: str, authenticated: bool = Depends(verify_token)):
    try:
        url = get_presigned_url(bucket_name, file_name)

        return JSONResponse(
            content={
                "success": "true",
                "file_url": url
            },
            status_code=200
        )
    except Exception as e:
        return JSONResponse(
            content={
                "error": str(e)
            },
            status_code=500
        )
