from .storage_providers import StorageProviders
from services.settings.settings import Settings
import logging
import boto3
from google.cloud import storage
from azure.storage.blob import BlobServiceClient
import tempfile
import os


class StorageConnection:
    storage_client = None
    storage_low_level_client = None

    def __init__(self, provider_name: str):
        self.settings = Settings.get_settings()
        match provider_name:
            case StorageProviders.aws.value:
                self.__connect_to_s3()
            case StorageProviders.azure.value:
                self.__connect_to_az()
            case StorageProviders.gcp.value:
                self.__connect_to_gcp()
            case _:
                logging.error(
                    f"[Storage Connection] Undefined provider: {provider_name}"
                )

    def __connect_to_s3(self):
        try:
            session = boto3.Session(
                aws_access_key_id=self.settings.aws_access_key,
                aws_secret_access_key=self.settings.aws_secret,
                region_name=self.settings.aws_region,
            )
            self.storage_client = session.resource("s3")
            self.storage_low_level_client = session.client("s3")
        except Exception as e:
            logging.error(f"[AWS S3 Client] Unable to connect to S3 client")
            logging.exception(e)

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
        try:
            self.storage_client = BlobServiceClient.from_connection_string(
                self.settings.azure_blob_connection_string
            )
        except Exception as e:
            logging.error(f"[Azure Client] Unable to connect to Azure client")
            logging.exception(e)
