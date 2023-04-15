from fastapi import FastAPI
from apis.api import router as api_router

app = FastAPI()

def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(api_router)

    return application


app = get_application()