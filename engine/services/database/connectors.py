# Add all connectors for various database
import logging
import boto3
import pymongo
import os

from .databases import Databases
from services.settings.settings import Settings


class DatabaseConnection:
    db_client = None
    _settings = Settings.get_settings()

    def __init__(self, db_name: str):
        match db_name:
            case Databases.mongodb.value:
                self.__connect_to_mongodb()
            case Databases.aws.value:
                self.__connect_to_aws()
            case _:
                logging.error(f"[DatabaseConnection] Undefined. Db provider: {db_name}")

    def __connect_to_mongodb(self):
        """Connect to MongoDB (Unimplemented)"""
        try:
            mongo_db_full_endpoint_url = f"mongodb://{self._settings.mongodb_db_username}:{self._settings.mongodb_db_password}@{self._settings.mongodb_db_endpoint}"
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
