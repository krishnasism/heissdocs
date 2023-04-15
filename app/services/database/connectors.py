# Add all connectors for various database
import logging
from .databases import Databases
import boto3
import os


class DatabaseConnection():
    db_client = None

    def __init__(self, db_name: str):
        match db_name:
            case Databases.mongodb.value:
                self.connect_to_mongodb()
            case Databases.aws.value:
                self.connect_to_aws()
            case _:
                logging.error("Undefined")

    def connect_to_mongodb(self):
        pass

    def connect_to_aws(self):
        session = boto3.Session(aws_access_key_id=os.getenv('AWS_ACCESS_KEY'), aws_secret_access_key=os.getenv(
            'AWS_SECRET'), region_name=os.getenv('AWS_REGION'))
        self.db_client = session.resource('dynamodb')
