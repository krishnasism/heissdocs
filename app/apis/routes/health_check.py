from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from services.security.verify_token import verify_token

router = APIRouter()


@router.get("/health-check/")
async def health_check():
    return JSONResponse(
        content={
            "message": "healthy",
        },
        status_code=200,
    )


@router.get("/auth-check/")
async def auth_check(authenticated: bool = Depends(verify_token)):
    return JSONResponse(
        content={
            "message": "success",
        },
        status_code=200,
    )
