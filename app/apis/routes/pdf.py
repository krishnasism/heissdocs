from fastapi import APIRouter, UploadFile, Form
from fastapi.responses import JSONResponse
from services.pdf.parsing.parser import get_pdf_body
from services.search.search import get_pdf_by_query
from services.summarize.summary import summarize_text
from services.storage.storage_ops import process_s3_files

from typing import Annotated

router = APIRouter()


@router.get("/search")
async def pdf_search(query: str):
    documents = get_pdf_by_query(query)
    return JSONResponse(
        content={
            "documents": documents
        },
        status_code=200
    )


@router.post("/upload")
async def upload_pdf(file: UploadFile, summarize: Annotated[str, Form()]):
    try:
        pdf_body = get_pdf_body(file)
        if summarize == "true":
            # TODO: Doesn't work as expected - keep False for now
            pdf_body = summarize_text(pdf_body)

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


@router.post("/process-s3-bucket")
async def process_s3_bucket(bucket_name: str):
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
