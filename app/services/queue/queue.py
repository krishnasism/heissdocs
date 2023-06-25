from .manager import get_local_sqs_client, get_queue_url
from .temp_storage_manager import upload_file_to_blob
from tempfile import NamedTemporaryFile
from uuid import uuid4
import logging
import json
from fastapi import UploadFile
from enums.QueueMessages import QueueMessageTypes
from services.storage.storage_ops import get_presigned_url, load_file_from_presigned_url
from tempfile import NamedTemporaryFile

TEMP_BUCKET_NAME = "tempfiles"  # TODO - Get from config


async def prepare_s3_job(
    bucket_name: str, key_name: str, user_email: str, viewer_bucket_name: str
) -> str:
    document_id = str(uuid4())
    blob_file_name = document_id + ".pdf"
    file_to_parse_url = get_presigned_url(
        bucket_name=bucket_name,
        blob_name=key_name,
        user_email=user_email,
    )
    params = {}
    file_to_parse = await load_file_from_presigned_url(file_to_parse_url)
    try:
        with NamedTemporaryFile(delete=True) as temp_file:
            temp_file.write(file_to_parse)
            temp_file.flush()
            with open(temp_file.name, "rb") as f:
                response = upload_file_to_blob(f, blob_file_name)
                if response:
                    logging.info("[Queue] File uploaded to temp bucket")

        params["temp_file_name"] = blob_file_name
        params["bucket_name"] = viewer_bucket_name
        params["temp_bucket_name"] = TEMP_BUCKET_NAME
        params["original_file_name"] = key_name
        params["user_email"] = user_email
        params["message_type"] = QueueMessageTypes.PARSING.value
        params["document_unique_id"] = blob_file_name

        send_queue_message(json.dumps(params))
        return blob_file_name
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    return None


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

    params["temp_file_name"] = blob_file_name
    params["temp_bucket_name"] = TEMP_BUCKET_NAME
    params["original_file_name"] = file.filename

    params["message_type"] = QueueMessageTypes.PARSING.value
    params["document_unique_id"] = blob_file_name
    send_queue_message(json.dumps(params))
    return blob_file_name


def send_queue_message(message: str):
    client = get_local_sqs_client()

    queue_url = get_queue_url(client, "parse_task")

    res = client.send_message(QueueUrl=queue_url, MessageBody=message)
    return True
