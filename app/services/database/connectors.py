# Add all connectors for various database
import logging
import boto3
import pymongo
import os

from .databases import Databases
from services.config import get_settings


class DatabaseConnection():
    db_client = None
    settings = get_settings()

    def __init__(self, db_name: str):
        match db_name:
            case Databases.mongodb.value:
                self._connect_to_mongodb()
            case Databases.aws.value:
                self._connect_to_aws()
            case _:
                logging.error("[DatabaseConnection] Undefined")

    def _connect_to_mongodb(self):
        mongo_db_full_endpoint_url = f"mongodb://{self.settings.mongodb_db_username}:{self.settings.mongodb_db_password}@{self.settings.mongodb_db_endpoint}"
        self.db_client = pymongo.MongoClient(mongo_db_full_endpoint_url)

    def _connect_to_aws(self):
        session = boto3.Session(aws_access_key_id=self.settings.aws_access_key, aws_secret_access_key=self.settings.aws_secret, region_name=self.settings.aws_region)
        self.db_client = session.resource('dynamodb')
