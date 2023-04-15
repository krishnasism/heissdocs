# Add all connectors for various database
import logging
import boto3
import pymongo
import os

from .databases import Databases


class DatabaseConnection():
    db_client = None

    def __init__(self, db_name: str):
        match db_name:
            case Databases.mongodb.value:
                self._connect_to_mongodb()
            case Databases.aws.value:
                self._connect_to_aws()
            case _:
                logging.error("[DatabaseConnection] Undefined")

    def _connect_to_mongodb(self):
        mongo_db_full_endpoint_url = f"mongodb://{os.getenv('MONGODB_DB_USERNAME')}:{os.getenv('MONGODB_DB_PASSWORD')}@{os.getenv('MONGODB_DB_ENDPOINT')}"
        self.db_client = pymongo.MongoClient(mongo_db_full_endpoint_url)

    def _connect_to_aws(self):
        session = boto3.Session(aws_access_key_id=os.getenv('AWS_ACCESS_KEY'), aws_secret_access_key=os.getenv(
            'AWS_SECRET'), region_name=os.getenv('AWS_REGION'))
        self.db_client = session.resource('dynamodb')
