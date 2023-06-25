from .storage_providers import StorageProviders
from settings.config import get_settings, override_settings
from settings.override_config import get_override_settings
import logging
import boto3


class StorageConnection:
    storage_client = None
    storage_low_level_client = None

    def __init__(self, provider_name: str, user_email: None):
        self.settings = override_settings(
            get_settings(), get_override_settings(user_email)
        )
        match provider_name:
            case StorageProviders.aws.value:
                self._connect_to_s3()
            case StorageProviders.azure.value:
                self._connect_to_az()
            case _:
                logging.error("[Storage Connection] Undefined")

    def _connect_to_s3(self):
        session = boto3.Session(
            aws_access_key_id=self.settings.aws_access_key,
            aws_secret_access_key=self.settings.aws_secret,
            region_name=self.settings.aws_region,
        )
        self.storage_client = session.resource("s3")
        self.storage_low_level_client = session.client("s3")

    def _connect_to_az(self):
        pass
