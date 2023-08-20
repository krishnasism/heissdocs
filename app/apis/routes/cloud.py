from fastapi import APIRouter, Depends, Form
from fastapi.responses import JSONResponse
from services.local.postgres import PostgresManager
from services.security.verify_token import verify_token
from services.storage.storage_ops import get_all_files
from services.queue.queue import prepare_cloud_job
from services.elasticsearch.elastic_ops import (
    fetch_scroll_elasticsearch_files,
    remove_elasticsearch_file,
)
from apis.requests.document_progress import DocumentProgressRequest
from enums.FileStages import FileStages
from typing import Annotated

import logging


router = APIRouter()

pm = PostgresManager()


@router.get("/all-bucket-files")
async def update_settings(
    bucket_name: str, user_email: str, authenticated: bool = Depends(verify_token)
):
    all_files = get_all_files(bucket_name, user_email)
    return JSONResponse(
        content={
            "all_files": all_files,
        },
        status_code=200,
    )


@router.post("/cloud-parsing-job")
async def cloud_parsing_job(
    source_bucket_name: Annotated[str, Form()],
    key_name: Annotated[str, Form()],
    user_email: Annotated[str, Form()],
    viewer_bucket_name: Annotated[str, Form()],
    authenticated: bool = Depends(verify_token),
):
    try:
        document_id = await prepare_cloud_job(
            source_bucket_name,
            key_name,
            user_email,
            viewer_bucket_name,
        )

        pm.create_documents_progress_entry(
            DocumentProgressRequest(
                userEmail=user_email,
                documentId=document_id,
                documentName=key_name,
                stage=FileStages.QUEUED.value,
                pagesParsed=0,
                totalPages=0,
            ).dict()
        )

        return JSONResponse(content={"message": "Created"}, status_code=201)
    except Exception as e:
        logging.error(e)
        return JSONResponse(content={"error": str(e)}, status_code=500)


@router.get("/all-elasticsearch-files")
async def get_all_elasticsearch_files(
    user_email: str,
    authenticated: bool = Depends(verify_token),
    scroll_id: str = None,
):
    all_files, scroll_id, error = await fetch_scroll_elasticsearch_files(
        user_email, scroll_id
    )
    return JSONResponse(
        content={
            "all_files": all_files,
            "scroll_id": scroll_id,
            "error": error,
        },
        status_code=200 if not error else 500,
    )


@router.delete("/elasticsearch-file")
async def delete_elasticsearch_file(
    user_email: Annotated[str, Form()],
    file_id: Annotated[str, Form()],
    authenticated: bool = Depends(verify_token),
):
    try:
        status = await remove_elasticsearch_file(
            user_email=user_email,
            file_id=file_id,
        )
        return JSONResponse(
            content={"message": "Deleted" if status else "Not Deleted"},
            status_code=200 if status else 500,
        )
    except Exception as e:
        logging.error(e)
        return JSONResponse(content={"error": str(e)}, status_code=500)
