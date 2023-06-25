from fastapi import APIRouter

from .routes import health_check, pdf, local, auth, cloud

router = APIRouter()
router.include_router(health_check.router, tags=["health_check"])
router.include_router(pdf.router, tags=["pdf"], prefix="/pdf")
router.include_router(local.router, tags=["local"])
router.include_router(auth.router, tags=["auth"], prefix="/auth")
router.include_router(cloud.router, tags=["cloud ops"], prefix="/cloud")
