from fastapi import FastAPI
from apis.api import router as api_router
from settings.env_loader import load_env_file

load_env_file()
app = FastAPI()

def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(api_router)

    return application


app = get_application()