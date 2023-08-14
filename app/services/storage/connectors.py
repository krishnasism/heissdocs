from .storage_providers import StorageProviders
from settings.config import get_settings, override_settings
from settings.override_config import get_override_settings
import logging
import boto3
from google.cloud import storage
import tempfile
import os


class StorageConnection:
    storage_client = None
    storage_low_level_client = None

    def __init__(self, provider_name: str, user_email: None):
        self.settings = override_settings(
            get_settings(), get_override_settings(user_email)
        )
        match provider_name:
            case StorageProviders.aws.value:
                self.__connect_to_s3()
            case StorageProviders.azure.value:
                self.__connect_to_az()
            case StorageProviders.gcp.value:
                self.__connect_to_gcp()
            case _:
                logging.error("[Storage Connection] Undefined")

    def __connect_to_s3(self):
        """Connect to AWS S3"""
        session = boto3.Session(
            aws_access_key_id=self.settings.aws_access_key,
            aws_secret_access_key=self.settings.aws_secret,
            region_name=self.settings.aws_region,
        )
        self.storage_client = session.resource("s3")
        self.storage_low_level_client = session.client("s3")

    def __connect_to_gcp(self):
        try:
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(self.settings.gcp_key_file_content.encode())
                temp_file_path = temp_file.name
            self.storage_client = storage.Client.from_service_account_json(
                temp_file_path
            )
            self.storage_low_level_client = None
            temp_file.close()
            if temp_file_path:
                os.unlink(temp_file_path)
        except Exception as e:
            logging.error(f"[GCP Client] Unable to connect to GCP client")
            logging.exception(e)

    def __connect_to_az(self):
        pass
