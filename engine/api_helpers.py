import logging
import time
from services.settings.api_token import APIToken
import httpx
import os

MAX_RETRIES = 20


def get_auth_token():
    retries = 0
    access_token = ""
    auth_endpoint = f"{os.environ['LOCAL_API_ENDPOINT']}/auth/get-token"  # TODO: Config

    while retries < MAX_RETRIES:
        try:
            auth_payload = {"userEmail": "xxx", "userKey": "yyy"}
            auth_res = httpx.post(auth_endpoint, data=auth_payload).json()
            access_token = auth_res.get("access_token")
            if not access_token:
                raise Exception("[Queue Handler] Unable to auth")
            else:
                logging.info("[Queue Handler] Auth successful")
                return access_token
        except:
            logging.exception("[Queue Handler] Unable to auth, please wait..")
        time.sleep(5)
        retries += 1

    if not access_token:
        logging.error("Unable to auth.")
        return None


def get_settings(user_email):
    apitoken_obj = APIToken.get_api_token()
    settings_endpoint = f"{os.environ['LOCAL_API_ENDPOINT']}/settings"
    headers = {"Authorization": "Bearer " + apitoken_obj.api_token}
    payload = {"userEmail": user_email}
    response = httpx.get(settings_endpoint, headers=headers, params=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def update_document_progress(document_progress: dict):
    apitoken_obj = APIToken.get_api_token()
    documents_progress_endpoint = (
        f"{os.environ['LOCAL_API_ENDPOINT']}/documents-progress"
    )
    headers = {"Authorization": "Bearer " + apitoken_obj.api_token}
    payload = {
        "userEmail": document_progress["user_email"],
        "documentId": document_progress["document_id"],
        "documentName": document_progress["document_name"],
        "stage": document_progress["stage"],
        "pagesParsed": str(document_progress["pages_parsed"]),
        "totalPages": str(document_progress["total_pages"]),
    }
    response = httpx.post(documents_progress_endpoint, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def post_log(log: dict):
    apitoken_obj = APIToken.get_api_token()
    documents_progress_endpoint = f"{os.environ['LOCAL_API_ENDPOINT']}/log"
    headers = {"Authorization": "Bearer " + apitoken_obj.api_token}
    response = httpx.post(documents_progress_endpoint, headers=headers, json=log)
    if response.status_code == 200:
        return response.json()
    else:
        return None
