from .storage_providers import StorageProviders
from services.config import get_settings
import logging
import boto3
import os

settings = get_settings()


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
        session = boto3.Session(aws_access_key_id=settings.aws_access_key,
                                aws_secret_access_key=settings.aws_secret, region_name=settings.aws_region)
        self.storage_client = session.resource('s3')

    def _connect_to_az(self):
        pass
