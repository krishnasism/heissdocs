from .connectors import StorageConnection
from .storage_providers import StorageProviders
from services.settings.settings import Settings
import logging
from azure.storage.blob import ContentSettings

def upload_file_to_bucket(filestream, filename_str: str, bucket=None) -> bool:
    """
    Upload file to configured cloud storage
    params: filestream: File stream (BufferedReader)
    params: filename_str: File name
    params: bucket: Bucket name
    return: bool: True if file uploaded successfully, False otherwise
    """
    _settings = Settings.get_settings()
    cloud_provider = _settings.cloud_provider
    match cloud_provider:
        case StorageProviders.aws.value:
            return upload_file_to_s3_bucket(filestream, filename_str, bucket)
        case StorageProviders.azure.value:
            return upload_file_to_az_blob(filestream, filename_str, bucket)
        case StorageProviders.gcp.value:
            return upload_file_to_gcp_bucket(filestream, filename_str, bucket)
        case _:
            logging.error(f"[Storage Connection] Undefined provider: {cloud_provider}")
            return False


def upload_file_to_az_blob(filestream, filename: str, bucket=None) -> bool:
    """
    Upload file to Azure blob
    params: filestream: File stream (BufferedReader)
    params: filename: File name
    params: bucket: Bucket name [Actually container name but whatever]
    return: bool: True if file uploaded successfully, False otherwise
    """
    storage_connection = StorageConnection(StorageProviders.azure.value)
    azure_storage_client = storage_connection.storage_client
    try:
        container_client = azure_storage_client.get_container_client(bucket)
        blob_client = container_client.get_blob_client(filename)
        content_settings = ContentSettings(content_type='application/pdf')
        blob_client.upload_blob(filestream, content_settings=content_settings)
        return True
    except Exception as e:
        logging.error(
            f"[Azure File Upload] Unable to upload file to container: {bucket}, file: {filename}"
        )
        logging.exception(e)
    return False


def upload_file_to_gcp_bucket(filestream, filename: str, bucket=None) -> bool:
    """
    Upload file to GCP bucket
    params: filestream: File stream (BufferedReader)
    params: filename: File name
    params: bucket: Bucket name
    return: bool: True if file uploaded successfully, False otherwise
    """
    storage_connection = StorageConnection(StorageProviders.gcp.value)
    try:
        gcp_storage_client = storage_connection.storage_client
        bucket = gcp_storage_client.bucket(bucket)
        blob = bucket.blob(filename)
        blob.upload_from_file(filestream, content_type="application/pdf")
        return True
    except Exception as e:
        logging.error(
            f"[GCP File Upload] Unable to upload file to bucket: {bucket}, file: {filename}"
        )
        logging.exception(e)
        return False


def upload_file_to_s3_bucket(filestream, filename: str, bucket=None) -> bool:
    """
    Upload file to S3 bucket
    params: filestream: File stream (BufferedReader)
    params: filename: File name
    params: bucket: Bucket name
    return: bool: True if file uploaded successfully, False otherwise
    """
    storage_connection = StorageConnection(StorageProviders.aws.value)
    s3_client = storage_connection.storage_client
    if not bucket:
        return False
    try:
        if ".pdf" in filename:
            pdf_object = s3_client.Object(bucket, filename)
            _ = pdf_object.put(Body=filestream, ContentType="application/pdf")
        else:
            pdf_object = s3_client.Object(bucket, filename)
            _ = pdf_object.put(Body=filestream)
    except Exception as e:
        logging.error(
            f"[AWSManager] Unable to upload file to bucket: {bucket}, file: {filename}"
        )
        logging.exception(e)
        return False
    return True


def get_s3_presigned_url(bucket_name: str, blob_name: str) -> str:
    """
    Get presigned url for S3 file
    params: bucket_name: Bucket name
    params: blob_name: Blob name
    return: str: Presigned url
    """
    storage_connection = StorageConnection(StorageProviders.aws.value)
    s3_client = storage_connection.storage_low_level_client
    try:
        url = s3_client.generate_presigned_url(
            ClientMethod="get_object",
            Params={"Bucket": bucket_name, "Key": blob_name},
            ExpiresIn=1800,
        )
        return url
    except Exception as e:
        logging.error(
            f"[AWSManager] Error: Unable to get presigned url bucket: {bucket_name}, blob: {blob_name}"
        )
        logging.exception(e)
        return ""
