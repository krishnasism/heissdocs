from .connectors import StorageConnection
from .storage_providers import StorageProviders
import logging
import httpx


async def load_file_from_presigned_url(url):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.content
    except Exception as e:
        logging.error(e)
        return None


def get_s3_presigned_url(bucket_name, blob_name, user_email):
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


def get_all_s3_files(bucket_name: str, user_email: str):
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
