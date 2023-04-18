from .storage_providers import StorageProviders
import logging
import boto3
import os


class StorageConnection():
    storage_client = None

    def __init__(self, provider_name: str):
        match provider_name:
            case StorageProviders.aws.value:
                self._connect_to_s3()
            case StorageProviders.azure.value:
                self._connect_to_az()
            case _:
                logging.error("[Storage Connection] Undefined")

    def _connect_to_s3(self):
        session = boto3.Session(aws_access_key_id=os.getenv('AWS_ACCESS_KEY'), aws_secret_access_key=os.getenv(
            'AWS_SECRET'), region_name=os.getenv('AWS_REGION'))
        self.storage_client = session.resource('s3')

    def _connect_to_az(self):
        pass
