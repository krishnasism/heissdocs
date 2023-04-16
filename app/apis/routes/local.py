from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/settings/", tags=["post-settings"])
def update_settings():
    return JSONResponse(
        content={
            "message": "updated",
        },
        status_code=200
    )


@router.get("/settings/", tags=["get-settings"])
def get_settings():
    return JSONResponse(
        content={
            "settings": {

            },
        },
        status_code=200
    )
