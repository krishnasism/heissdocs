from fastapi import APIRouter
from services.local.postgres import PostgresManager
import http.client
from settings.config import get_settings
import json


router = APIRouter()
pm = PostgresManager()
settings = get_settings()


@router.post("/get-token")
async def get_token():
    conn = http.client.HTTPSConnection(settings.auth0_domain)

    payload = {
        "client_id": settings.auth0_client_id,
        "client_secret": settings.auth0_client_secret,
        "audience": settings.auth0_api_audience,
        "grant_type": "client_credentials",
    }

    headers = {"content-type": "application/json"}

    conn.request("POST", "/oauth/token", json.dumps(payload), headers)

    res = conn.getresponse()
    data = res.read()

    return json.loads(data.decode("utf-8"))
