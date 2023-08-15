# Add all connectors for various database
import logging
import boto3
import pymongo

from .databases import Databases
from settings.config import get_settings, override_settings
from settings.override_config import get_override_settings
import tempfile
import google.cloud.firestore as firestore
import os


class DatabaseConnection:
    db_client = None

    def __init__(self, db_name: str, user_email: None):
        self.settings = override_settings(
            get_settings(), get_override_settings(user_email)
        )
        match db_name:
            case Databases.mongodb.value:
                self.__connect_to_mongodb()
            case Databases.aws.value:
                self.__connect_to_aws_dynamodb()
            case Databases.gcp.value:
                self.__connect_to_gcp_firestore()
            case _:
                logging.error("[DatabaseConnection] Undefined")

    def __connect_to_mongodb(self):
        """Connect to MongoDB"""
        try:
            mongo_db_full_endpoint_url = f"mongodb+srv://{self.settings.mongo_db_username}:{self.settings.mongo_db_password}@{self.settings.mongo_db_database}.{self.settings.mongo_db_host}"
            self.db_client = pymongo.MongoClient(mongo_db_full_endpoint_url)
        except Exception as e:
            logging.error(f"[MongoDB Connection] {e}")

    def __connect_to_aws_dynamodb(self):
        """Connect to AWS DynamoDB"""
        session = boto3.Session(
            aws_access_key_id=self.settings.aws_access_key,
            aws_secret_access_key=self.settings.aws_secret,
            region_name=self.settings.aws_region,
        )
        self.db_client = session.resource("dynamodb")

    def __connect_to_gcp_firestore(self):
        """Connect to GCP Firestore"""
        try:
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(self.settings.gcp_key_file_content.encode())
                temp_file_path = temp_file.name
            self.db_client = firestore.Client.from_service_account_json(temp_file_path)
            self.storage_low_level_client = None
            temp_file.close()
            if temp_file_path:
                os.unlink(temp_file_path)
        except Exception as e:
            logging.error(f"[GCP Client] Unable to connect to GCP client")
            logging.exception(e)
