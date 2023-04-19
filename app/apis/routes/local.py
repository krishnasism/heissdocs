from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from services.local.settings import get_settings, set_settings
from apis.requests.settings import Settings
from typing import Annotated

router = APIRouter()


@router.post("/settings", tags=["post-settings"])
def update_settings(settings: Settings):
    return JSONResponse(
        content={
            "message": "updated",
        },
        status_code=200
    )


@router.get("/settings", tags=["get-settings"])
def get_settings():
    return JSONResponse(
        content={
            "settings": {

            },
        },
        status_code=200
    )
