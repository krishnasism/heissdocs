import requests
import logging
import time
import json
from temp_storage_manager import get_temp_file_stream, delete_file
from services.pdf.parsing.parser import get_pdf_body
from tempfile import NamedTemporaryFile
from services.storage.storage_ops import upload_file_to_blob
from services.database.db_ops import put_pdf_to_database

from uuid import uuid4
import os

MAX_RETRIES = 20


def get_auth_token():
    retries = 0
    access_token = ''
    auth_endpoint = 'http://app:8000/auth/get-token'  # TODO: Config

    while retries < MAX_RETRIES:
        try:
            auth_payload = {
                'userEmail': 'xxx',
                'userKey': 'yyy'
            }
            auth_res = requests.post(
                auth_endpoint, data=auth_payload).json()
            access_token = auth_res.get('access_token')
            if not access_token:
                raise Exception('[Queue Handler] Unable to auth')
            else:
                return access_token
        except:
            logging.error('[Queue Handler] Unable to auth, please wait..')
        time.sleep(5)
        retries += 1

    if not access_token:
        logging.error("Unable to auth.")
        return None


def process_file(message):
    file_params = json.loads(message)

    file_stream = get_temp_file_stream(
        file_params['temp_file_name'], file_params['temp_bucket_name'])

    temp_file = NamedTemporaryFile(delete=False)
    with open(temp_file.name, 'wb') as f:
        f.write(file_stream)

    pdf_body, file_metadata = get_pdf_body(pdf_file=temp_file,
                                           original_file_name=(
                                               file_params['original_file_name']),
                                           store_files_in_cloud=file_params['store_files_in_cloud'],
                                           bucket_name=file_params['bucket_name'],
                                           )

    if file_params['store_files_in_cloud']:
        blob_file_name = str(uuid4()) + ".pdf"
        bucket_name = file_params['bucket_name']
        with open(temp_file.name, "rb") as f:
            if bucket_name:
                response = upload_file_to_blob(f, blob_file_name, bucket_name)
                if response:
                    file_metadata['s3_blob_file_name'] = blob_file_name
                    file_metadata['s3_bucket_name'] = bucket_name

    status = put_pdf_to_database(pdf_body, file_metadata)
    temp_file.close()
    os.remove(temp_file.name)
    try:
        delete_file(file_params['temp_file_name'],
                    file_params['temp_bucket_name'])
    except:
        logging.warning('[Process] File could not be deleted from S3')

    if status:
        return True
    else:
        return False


def get_settings(user_email, api_token):
    settings_endpoint = 'http://app:8000/settings'
    headers = {
        'Authorization': 'Bearer ' + api_token
    }
    payload = {
        'userEmail': user_email
    }
    response = requests.request(
        "GET", settings_endpoint, headers=headers, params=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return None
