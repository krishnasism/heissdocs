from fastapi import APIRouter, Depends, Query
from fastapi.responses import JSONResponse
from apis.requests.settings import Settings
from apis.requests.document_progress import DocumentProgressRequest
from apis.requests.log_request import LogRequest
from services.local.postgres import PostgresManager
from services.utils.helpers import convert_dict_to_camel_case
from services.security.verify_token import verify_token
from enums.QueueMessages import QueueMessageTypes
from services.queue.queue import send_queue_message
import json
from datetime import datetime

router = APIRouter()

pm = PostgresManager()


@router.post("/settings")
async def update_settings(
    settings: Settings,
    authenticated: bool = Depends(verify_token),
):
    new_settings_obj = {k: v for k, v in settings.model_dump().items() if v is not None}
    pm.update_settings(new_settings_obj)
    q_params = {}
    q_params["message_type"] = QueueMessageTypes.SETTINGS_UPDATED.value
    q_params["user_email"] = settings.userEmail
    send_queue_message(json.dumps(q_params))

    return JSONResponse(
        content={
            "message": "updated",
        },
        status_code=200,
    )


@router.get("/settings")
async def get_settings(userEmail: str, authenticated: bool = Depends(verify_token)):
    settings = convert_dict_to_camel_case(pm.get_settings(userEmail))
    return JSONResponse(
        content={
            "settings": settings,
        },
        status_code=200,
    )


@router.get("/refresh-queue-settings")
async def refresh_queue_settings(
    userEmail: str, authenticated: bool = Depends(verify_token)
):
    q_params = {}
    q_params["message_type"] = QueueMessageTypes.SETTINGS_UPDATED.value
    q_params["user_email"] = userEmail
    send_queue_message(json.dumps(q_params))
    return JSONResponse(
        content={
            "message": "Queue Refreshed",
        },
        status_code=200,
    )


@router.get("/documents-progress")
async def get_documents_in_progress(
    userEmail: str, authenticated: bool = Depends(verify_token)
):
    documents = pm.get_documents_progress(userEmail)
    for document in documents:
        del document["updated_on"]
    return JSONResponse(content={"documents": documents}, status_code=200)


@router.post("/documents-progress")
async def set_documents_in_progress(
    documentsProgressRequest: DocumentProgressRequest,
    authenticated: bool = Depends(verify_token),
):
    pm.update_documents_progress(documentsProgressRequest.model_dump())
    return JSONResponse(content={"message": "success"}, status_code=200)


@router.post("/log")
async def post_log(
    logRequest: LogRequest,
    authenticated: bool = Depends(verify_token),
):
    pm.post_log(logRequest.model_dump())
    return JSONResponse(content={"message": "success"}, status_code=200)


@router.get("/logs")
async def get_logs(
    user_email: str,
    start_time: str = Query(None, description="Start time in ISO 8601 format"),
    end_time: str = Query(None, description="End time in ISO 8601 format"),
    authenticated: bool = Depends(verify_token),
):
    if start_time and end_time:
        start_datetime = datetime.fromisoformat(start_time)
        end_datetime = datetime.fromisoformat(end_time)
        logs = pm.get_logs_in_time_range(user_email, start_datetime, end_datetime)
    else:
        logs = pm.get_logs(user_email)
    return JSONResponse(content={"logs": logs}, status_code=200)
