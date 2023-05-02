from .connectors import StorageConnection
from .storage_providers import StorageProviders
import logging

def get_presigned_url(bucket_name, blob_name):
    storage_connection = StorageConnection(StorageProviders.aws.value)
    s3_client = storage_connection.storage_low_level_client
    try:
        url = s3_client.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': bucket_name,
                'Key': blob_name
            },
            ExpiresIn=1800
        )
        return url
    except Exception as e:
        logging.error(e)
        return ""
