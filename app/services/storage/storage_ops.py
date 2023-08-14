from .connectors import StorageConnection
from .storage_providers import StorageProviders
import logging
import httpx
from settings.config import get_settings, override_settings
from settings.override_config import get_override_settings
from google.cloud import storage
import datetime


async def load_file_from_presigned_url(url: str) -> bytes:
    """
    Load file from presigned url
    params: url: Presigned url
    return: bytes: File content
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.content
    except Exception as e:
        logging.error(e)
        return None


def get_gcp_signed_url(
    bucket_name: str,
    blob_name: str,
    user_email: str,
):
    """
    Get signed URL for Google Cloud Storage blob
    params: bucket_name: Bucket name
    params: blob_name: Blob name
    params: expiration_seconds: Expiration time in seconds
    return: str: Signed URL
    """
    try:
        storage_connection = StorageConnection(StorageProviders.gcp.value, user_email)
        gcp_client = storage_connection.storage_client
        bucket = gcp_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        signed_url = blob.generate_signed_url(
            version="v4", expiration=datetime.timedelta(minutes=15), method="GET"
        )
        return signed_url
    except Exception as e:
        logging.error("[GCP] Error generating signed url")
        logging.exception(e)
        return ""


def get_cloud_presigned_url(bucket_name: str, blob_name: str, user_email: str) -> str:
    settings = override_settings(get_settings(), get_override_settings(user_email))
    cloud_provider = settings.cloud_provider
    match cloud_provider:
        case StorageProviders.aws.value:
            return get_s3_presigned_url(
                bucket_name=bucket_name, blob_name=blob_name, user_email=user_email
            )
        case StorageProviders.azure.value:
            return get_azure_presigned_url(
                bucket_name=bucket_name, blob_name=blob_name, user_email=user_email
            )
        case StorageProviders.gcp.value:
            return get_gcp_signed_url(
                bucket_name=bucket_name, blob_name=blob_name, user_email=user_email
            )
        case _:
            logging.error(f"[Storage Connection] Undefined provider: {cloud_provider}")


def get_azure_presigned_url(bucket_name: str, blob_name: str, user_email: str) -> str:
    return ""


def get_s3_presigned_url(bucket_name: str, blob_name: str, user_email: str) -> str:
    """
    Get presigned url for S3 file
    params: bucket_name: Bucket name
    params: blob_name: Blob name
    params: user_email: User email
    return: str: Presigned url
    """
    storage_connection = StorageConnection(StorageProviders.aws.value, user_email)
    s3_client = storage_connection.storage_low_level_client
    try:
        url = s3_client.generate_presigned_url(
            ClientMethod="get_object",
            Params={"Bucket": bucket_name, "Key": blob_name},
            ExpiresIn=1800,
        )
        return url
    except Exception as e:
        logging.error(e)
        return ""


def get_all_files(bucket_name: str, user_email: str) -> dict:
    settings = override_settings(get_settings(), get_override_settings(user_email))
    cloud_provider = settings.cloud_provider
    match cloud_provider:
        case StorageProviders.aws.value:
            return get_all_s3_files(bucket_name=bucket_name, user_email=user_email)
        case StorageProviders.azure.value:
            return get_all_azure_files(bucket_name=bucket_name, user_email=user_email)
        case StorageProviders.gcp.value:
            return get_all_gcp_files(bucket_name=bucket_name, user_email=user_email)
        case _:
            logging.error(f"[Storage Connection] Undefined provider: {cloud_provider}")


def get_all_azure_files(bucket_name: str, user_email: str) -> dict:
    return {"files": [], "error": "Not implemented"}


def get_all_gcp_files(bucket_name: str, user_email: str) -> dict:
    """
    Get all files from GCP bucket
    params: bucket_name: Bucket name
            user_email: User email
    return: dict: Files list
    """
    try:
        storage_connection = StorageConnection(StorageProviders.gcp.value, user_email)
        gcp_client = storage_connection.storage_client
        bucket = gcp_client.bucket(bucket_name)
        files_list = [blob.name for blob in bucket.list_blobs()]
        result = {"files": files_list, "error": None}
        return result
    except Exception as e:
        logging.error("[Storage S3] Something went wrong", str(e))
        return {"files": None, "error": str(e)}


def get_all_s3_files(bucket_name: str, user_email: str) -> dict:
    """
    Get all files from S3 bucket
    params: bucket_name: Bucket name
            user_email: User email
    return: dict: Files list
    """
    try:
        storage_connection = StorageConnection(StorageProviders.aws.value, user_email)
        s3_client = storage_connection.storage_client
        bucket = s3_client.Bucket(bucket_name)
        return {
            "files": [bucket_obj.key for bucket_obj in bucket.objects.all()],
            "error": None,
        }
    except Exception as e:
        logging.error("[Storage S3] Something went wrong", str(e))
        return {"files": None, "error": str(e)}
