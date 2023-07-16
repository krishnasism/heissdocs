from .connectors import StorageConnection
from .storage_providers import StorageProviders
import logging


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
        logging.error(f"[AWSManager] Unable to upload file to bucket: {bucket}, file: {filename}")
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
        logging.error(f"[AWSManager] Error: Unable to get presigned url bucket: {bucket_name}, blob: {blob_name}")
        logging.exception(e)
        return ""
