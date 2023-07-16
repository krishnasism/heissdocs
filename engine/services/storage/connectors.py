from .storage_providers import StorageProviders
from services.settings.settings import Settings
import logging
import boto3


class StorageConnection:
    storage_client = None
    storage_low_level_client = None

    def __init__(self, provider_name: str):
        match provider_name:
            case StorageProviders.aws.value:
                self.__connect_to_s3()
            case StorageProviders.azure.value:
                self.__connect_to_az()
            case _:
                logging.error(f"[Storage Connection] Undefined provider: {provider_name}")

    def __connect_to_s3(self):
        _settings = Settings.get_settings()
        try:
            session = boto3.Session(
                aws_access_key_id=_settings.aws_access_key,
                aws_secret_access_key=_settings.aws_secret,
                region_name=_settings.aws_region,
            )
            self.storage_client = session.resource("s3")
            self.storage_low_level_client = session.client("s3")
        except Exception as e:
            logging.error(f"[Azure S3 Client] Unable to connect to S3 client")
            logging.exception(e)

    def __connect_to_az(self):
        """Unimplemented"""
        pass
