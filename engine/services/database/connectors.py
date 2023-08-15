# Add all connectors for various database
import logging
import boto3
import pymongo

from .databases import Databases
from services.settings.settings import Settings
import tempfile
import google.cloud.firestore as firestore
from azure.cosmos import CosmosClient
import os


class DatabaseConnection:
    db_client = None
    _settings = Settings.get_settings()

    def __init__(self, db_name: str):
        match db_name:
            case Databases.mongodb.value:
                self.__connect_to_mongodb()
            case Databases.aws.value:
                self.__connect_to_aws()
            case Databases.gcp.value:
                self.__connect_to_gcp()
            case Databases.azure.value:
                self.__connect_to_azure()
            case _:
                logging.error(f"[DatabaseConnection] Undefined. Db provider: {db_name}")

    def __connect_to_mongodb(self):
        """Connect to MongoDB"""
        try:
            mongo_db_full_endpoint_url = f"mongodb+srv://{self._settings.mongo_db_username}:{self._settings.mongo_db_password}@{self._settings.mongo_db_database}.{self._settings.mongo_db_host}"
            self.db_client = pymongo.MongoClient(mongo_db_full_endpoint_url)
        except Exception as e:
            logging.error(f"[MongoDB Connection] {e}")

    def __connect_to_aws(self):
        """Connect to AWS DynamoDB"""
        try:
            session = boto3.Session(
                aws_access_key_id=self._settings.aws_access_key,
                aws_secret_access_key=self._settings.aws_secret,
                region_name=self._settings.aws_region,
            )
            self.db_client = session.resource("dynamodb")
        except Exception as e:
            logging.error(
                f"[AWS DynamoDB Connection] Unable to connect to DynamoDB client"
            )
            logging.exception(e)

    def __connect_to_gcp(self):
        """Connect to GCP Firestore"""
        try:
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(self._settings.gcp_key_file_content.encode())
                temp_file_path = temp_file.name
            self.db_client = firestore.Client.from_service_account_json(temp_file_path)
            self.storage_low_level_client = None
            temp_file.close()
            if temp_file_path:
                os.unlink(temp_file_path)
        except Exception as e:
            logging.error(f"[GCP Client] Unable to connect to GCP client")
            logging.exception(e)

    def __connect_to_azure(self):
        try:
            self.db_client = CosmosClient(
                self._settings.cosmos_db_host, self._settings.cosmos_db_key
            )
        except Exception as e:
            logging.error(f"[Azure CosmosDB] Unable to connect to Azure client")
            logging.exception(e)
