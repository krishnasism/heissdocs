from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/health-check/", tags=["health-check"])
def health_check():
    return JSONResponse(
        content={
            "message": "healthy",
        },
        status_code=200
    )
