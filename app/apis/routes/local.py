from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from apis.requests.settings import Settings
from apis.requests.document_progress import DocumentProgressRequest
from services.local.postgres import PostgresManager
from services.utils.helpers import convert_dict_to_camel_case
from services.security.verify_token import verify_token
from enums.QueueMessages import QueueMessageTypes
from services.queue.queue import send_queue_message
import json

router = APIRouter()

pm = PostgresManager()


@router.post("/settings")
async def update_settings(
    settings: Settings, authenticated: bool = Depends(verify_token)
):
    pm.update_settings(settings.dict())
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
    return JSONResponse(content={"documents": documents}, status_code=200)


@router.post("/documents-progress")
async def set_documents_in_progress(
    documentsProgressRequest: DocumentProgressRequest,
    authenticated: bool = Depends(verify_token),
):
    pm.update_documents_progress(documentsProgressRequest.dict())
    return JSONResponse(content={"message": "success"}, status_code=200)
