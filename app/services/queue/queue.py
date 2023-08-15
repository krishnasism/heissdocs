from .manager import get_local_sqs_client, get_queue_url
from .temp_storage_manager import upload_file_to_temp_s3_bucket
from settings.config import get_settings, override_settings
from settings.override_config import get_override_settings
from services.storage.storage_providers import StorageProviders
from tempfile import NamedTemporaryFile
from uuid import uuid4
import logging
import json
from fastapi import UploadFile
from enums.QueueMessages import QueueMessageTypes
from services.storage.storage_ops import (
    get_s3_presigned_url,
    get_gcp_signed_url,
    get_azure_sas_link,
    load_file_from_presigned_url,
)
from tempfile import NamedTemporaryFile
import pypdf

TEMP_BUCKET_NAME = "tempfiles"  # TODO - Get from config


async def prepare_cloud_job(
    bucket_name: str, key_name: str, user_email: str, viewer_bucket_name: str
) -> str:
    settings = override_settings(get_settings(), get_override_settings(user_email))
    match settings.cloud_provider:
        case StorageProviders.aws.value:
            return await prepare_s3_job(
                bucket_name=bucket_name,
                key_name=key_name,
                user_email=user_email,
                viewer_bucket_name=viewer_bucket_name,
            )
        case StorageProviders.azure.value:
            return await prepare_azure_job(
                bucket_name=bucket_name,
                key_name=key_name,
                user_email=user_email,
                viewer_bucket_name=viewer_bucket_name,
            )
        case StorageProviders.gcp.value:
            return await prepare_gcp_job(
                bucket_name=bucket_name,
                key_name=key_name,
                user_email=user_email,
                viewer_bucket_name=viewer_bucket_name,
            )
        case _:
            logging.error("[Storage Connection] Undefined")


async def process_file_url(
    document_id,
    file_to_parse_url,
    destination_bucket_name,
    user_email,
    original_file_name,
    blob_file_name,
):
    params = {}
    file_to_parse = await load_file_from_presigned_url(file_to_parse_url)
    try:
        with NamedTemporaryFile(delete=True) as temp_file:
            temp_file.write(file_to_parse)
            temp_file.flush()
            chunks, total_pages = split_pdf_into_chunks(temp_file.name, 50)
            for i in range(0, len(chunks)):
                chunk_file_name = f"{document_id}_part{i}.pdf"
                res = upload_file_to_temp_s3_bucket(chunks[i], chunk_file_name)
                if res:
                    logging.info(
                        f"[Prepare Job S3] File part {i} uploaded to temp bucket"
                    )

        params["chunk_file_name"] = chunk_file_name
        params["temp_bucket_name"] = TEMP_BUCKET_NAME
        params["original_file_name"] = original_file_name
        params["user_email"] = user_email
        params["message_type"] = QueueMessageTypes.PARSING.value
        params["document_unique_id"] = blob_file_name
        params["total_pages"] = total_pages
        params["bucket_name"] = destination_bucket_name

        send_queue_message(json.dumps(params))
        return blob_file_name
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    return None


async def prepare_azure_job(
    bucket_name: str, key_name: str, user_email: str, viewer_bucket_name: str
) -> str:
    document_id = str(uuid4())
    blob_file_name = document_id + ".pdf"
    file_to_parse_url = get_azure_sas_link(
        bucket_name=bucket_name,
        blob_name=key_name,
        user_email=user_email,
    )
    return await process_file_url(
        document_id,
        file_to_parse_url,
        viewer_bucket_name,
        user_email,
        key_name,
        blob_file_name,
    )


async def prepare_gcp_job(
    bucket_name: str, key_name: str, user_email: str, viewer_bucket_name: str
) -> str:
    """
    Prepare job for reading file from s3 bucket and send job to parsing queue
    params: bucket_name: bucket name
    params: key_name: key name (file name)
    params: user_email: User email
    params: viewer_bucket_name: Viewer bucket name (where the parsed file will be uploaded)
    return: str: Document name in viewer bucket
    """
    document_id = str(uuid4())
    blob_file_name = document_id + ".pdf"
    file_to_parse_url = get_gcp_signed_url(
        bucket_name=bucket_name,
        blob_name=key_name,
        user_email=user_email,
    )
    return await process_file_url(
        document_id,
        file_to_parse_url,
        viewer_bucket_name,
        user_email,
        key_name,
        blob_file_name,
    )


async def prepare_s3_job(
    bucket_name: str, key_name: str, user_email: str, viewer_bucket_name: str
) -> str:
    """
    Prepare job for reading file from s3 bucket and send job to parsing queue
    params: bucket_name: S3 bucket name
    params: key_name: S3 key name (file name)
    params: user_email: User email
    params: viewer_bucket_name: Viewer bucket name (where the parsed file will be uploaded)
    return: str: Document name in viewer bucket
    """
    document_id = str(uuid4())
    blob_file_name = document_id + ".pdf"
    file_to_parse_url = get_s3_presigned_url(
        bucket_name=bucket_name,
        blob_name=key_name,
        user_email=user_email,
    )
    return await process_file_url(
        document_id,
        file_to_parse_url,
        viewer_bucket_name,
        user_email,
        key_name,
        blob_file_name,
    )


def prepare_job(file: UploadFile, params: dict) -> dict:
    """
    Prepare job for parsing queue
    params: UploadFile: File to parse
    params: dict: Additional params
    return: dict: File metadata
    """
    temp_file = NamedTemporaryFile(delete=False)
    document_id = str(uuid4())
    try:
        file_contents = file.file.read()
        with temp_file as f:
            f.write(file_contents)
    except:
        return ""
    blob_file_name = document_id + ".pdf"

    # Create chunks of PDF file before sending to queue
    # This will help in parallel processing of PDF file
    # And not overwhelm the worker (set to 50 pages/file for now)
    chunks, total_pages = split_pdf_into_chunks(temp_file.name, 50)
    with open(temp_file.name, "rb") as f:
        response = upload_file_to_temp_s3_bucket(f, blob_file_name)
        if response:
            logging.info("[Queue] File uploaded to temp bucket")

    for i in range(0, len(chunks)):
        chunk_file_name = f"{document_id}_part{i}.pdf"
        res = upload_file_to_temp_s3_bucket(chunks[i], chunk_file_name)
        if res:
            logging.info(f"[Prepare Job] File part {i} uploaded to temp bucket")

        params["chunk_file_name"] = chunk_file_name
        params["temp_bucket_name"] = TEMP_BUCKET_NAME
        params["original_file_name"] = file.filename
        params["message_type"] = QueueMessageTypes.PARSING.value
        params["document_unique_id"] = blob_file_name
        params["total_pages"] = total_pages
        send_queue_message(json.dumps(params))

    return {
        "document_id": f"{document_id}.pdf",
        "total_pages": total_pages,
    }


def send_queue_message(message: str) -> bool:
    """
    Send message to SQS queue
    params: str: Message to send
    return: bool: True
    """
    try:
        client = get_local_sqs_client()

        queue_url = get_queue_url(client, "parse_task")

        _ = client.send_message(QueueUrl=queue_url, MessageBody=message)
        logging.info("[Queue] Message sent to queue")
        return True
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return False


def split_pdf_into_chunks(file_path: str, chunk_size: int = 50):
    """
    Split PDF file into chunks
    params: file_path: File path
    params: chunk_size: Chunk size
    return: list: List of chunks
    """
    pdf = pypdf.PdfReader(file_path)
    total_pages = len(pdf.pages)

    chunks = []
    for start_page in range(0, total_pages, chunk_size):
        end_page = min(start_page + chunk_size, total_pages)
        chunk_pdf = pypdf.PdfWriter()
        for page_num in range(start_page, end_page):
            chunk_pdf.add_page(pdf.pages[page_num])

        temp_file = NamedTemporaryFile(delete=False)
        with open(temp_file.name, "wb") as f:
            chunk_pdf.write(f)

        chunks.append(temp_file)

    return (chunks, total_pages)
