from fastapi import APIRouter

from .routes import health_check, pdf, local

router = APIRouter()
router.include_router(health_check.router, tags=["health_check"])
router.include_router(pdf.router, tags=["pdf"], prefix="/pdf")
router.include_router(local.router, tags=["local"])
