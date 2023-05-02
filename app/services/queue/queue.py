from .manager import get_local_sqs_client, get_queue_url
from .temp_storage_manager import upload_file_to_blob
from tempfile import NamedTemporaryFile
from uuid import uuid4
import logging
import json
from fastapi import UploadFile
from enums.QueueMessages import QueueMessageTypes

TEMP_BUCKET_NAME = 'tempfiles'  # TODO - Get from config


def prepare_job(file: UploadFile, params) -> str:
    temp_file = NamedTemporaryFile(delete=False)
    try:
        file_contents = file.file.read()
        with temp_file as f:
            f.write(file_contents)
    except:
        return ""
    blob_file_name = str(uuid4()) + ".pdf"
    with open(temp_file.name, "rb") as f:
        response = upload_file_to_blob(f, blob_file_name)
        if response:
            logging.info("[Queue] File uploaded to temp bucket")

    params['temp_file_name'] = blob_file_name
    params['temp_bucket_name'] = TEMP_BUCKET_NAME
    params['original_file_name'] = file.filename

    params['message_type'] = QueueMessageTypes.PARSING.value
    params['document_unique_id'] = blob_file_name
    send_queue_message(json.dumps(params))
    return blob_file_name

def send_queue_message(message: str):
    client = get_local_sqs_client()

    queue_url = get_queue_url(client, 'parse_task')

    res = client.send_message(
        QueueUrl=queue_url,
        MessageBody=message
    )
    return True
