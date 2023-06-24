from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from services.local.postgres import PostgresManager
from services.security.verify_token import verify_token
from services.storage.storage_ops import get_all_s3_files
from services.queue.queue import prepare_job

router = APIRouter()

pm = PostgresManager()


@router.get("/all-bucket-files")
async def update_settings(bucket_name: str, user_email: str, authenticated: bool = Depends(verify_token)):
    s3_response = get_all_s3_files(bucket_name, user_email)
    return JSONResponse(
        content={
            "s3_response": s3_response,
        },
        status_code=200
    )


@router.post("/s3-parsing-job")
async def s3_parsing_job(bucket_name: str, key_name: str, user_email: str, authenticated: bool = Depends(verify_token)):
    # TODO:
    # 1. Create job entry in database for progress tracking / elimination from list in cloud interface
    # 2. Create queue job
    # 3. Add function in queue to handle s3 job
    return JSONResponse(
        content={
            "message": "queued",
        },
        status_code=201
    )
