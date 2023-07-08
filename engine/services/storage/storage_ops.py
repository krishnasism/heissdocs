from .connectors import StorageConnection
from .storage_providers import StorageProviders
import logging


def upload_file_to_s3_bucket(filestream, filename, bucket=None):
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
        logging.error(f"[AWSManager] Error: {str(e)}")
        return False
    return True



def get_s3_presigned_url(bucket_name, blob_name):
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
        logging.error(e)
        return ""
