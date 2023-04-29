import requests
import logging
import time
import json
from temp_storage_manager import get_temp_file_stream, delete_file
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


def process_file(message, api_token):
    upload_endpoint = 'http://app:8000/pdf/upload'  # TODO: Config

    file_params = json.loads(message)
    payload = {'summarize': file_params['summarize'],
               'user_email': file_params['user_email'],
               'store_files_in_cloud': file_params['store_files_in_cloud'],
               'bucket_name': file_params['bucket_name']}

    headers = {
        'Authorization': 'Bearer ' + api_token
    }
    file_stream = get_temp_file_stream(
        file_params['temp_file_name'], file_params['temp_bucket_name'])

    files = [
        ('file', (file_params['original_file_name'],
         file_stream, 'application/pdf'))
    ]
    response = requests.request(
        "POST", upload_endpoint, headers=headers, data=payload, files=files)
    try:
        delete_file(file_params['temp_file_name'],
                    file_params['temp_bucket_name'])
    except:
        pass
    if response.status_code == 200:
        return True
    else:
        return False
