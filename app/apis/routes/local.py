from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from services.local.settings import get_settings, set_settings
from apis.requests.settings import Settings
from typing import Annotated
from services.local.postgres import PostgresManager
from services.utils.helpers import convert_dict_to_camel_case

router = APIRouter()

pm = PostgresManager()


@router.post("/settings")
def update_settings(settings: Settings):
    pm.update_settings(settings.dict())
    return JSONResponse(
        content={
            "message": "updated",
        },
        status_code=200
    )


@router.get("/settings")
def get_settings(userEmail: str):
    settings = convert_dict_to_camel_case(pm.get_settings(userEmail))
    return JSONResponse(
        content={
            "settings": settings,
        },
        status_code=200
    )
