from .connectors import DatabaseConnection
from .databases import Databases
from datetime import datetime
from uuid import uuid4
import logging
import os

# TODO: This needs to come from config
CONFIGURED_DB = os.getenv("DOCUMENT_DB_PROVIDER")  
AWS_SEARCH_TABLE_NAME = os.getenv("AWS_SEARCH_TABLE_NAME")  # TODO: Needs to come from config
MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME") # TODO: Needs to come from config
MONGODB_COLLECTION_NAME = os.getenv("MONGODB_COLLECTION_NAME") # TODO: Needs to come from config

def put_pdf_to_database(pdf_body, file_metadata):
    configured_db = os.getenv("DOCUMENT_DB_PROVIDER")  
    database_connection = DatabaseConnection(os.getenv("DOCUMENT_DB_PROVIDER"))
    match configured_db:
        case Databases.mongodb.value:
            return _put_pdf_body_mongodb(database_connection.db_client, pdf_body, file_metadata, database_name=MONGODB_DB_NAME, table_name=MONGODB_COLLECTION_NAME)
        case Databases.aws.value:
            return _put_pdf_body_dynamodb(database_connection.db_client, pdf_body, file_metadata, table_name=os.getenv("AWS_SEARCH_TABLE_NAME"))
        case _:
            logging.error("[DB Ops - Document DB] Undefined provider")
            pass


def _put_pdf_body_dynamodb(dynamodb, pdfbody, metadata, table_name):
    try:
        table = dynamodb.Table(table_name)
        for page_num, page_data in pdfbody.items():
            table.put_item(Item={
                "pdf_body": str(page_data),
                "file_name":  f"{str(metadata.get('filename'))}_{str(uuid4().hex)}",
                "made_on": str(datetime.utcnow()),
                "page_num": str(page_num)
            })
    except Exception as e:
        logging.error(f"[DB Ops - DynamoDB] Error: {str(e)}")
        return False
    return True


def _put_pdf_body_mongodb(mongodb, pdfbody, metadata, database_name, table_name):
    try:
        db = mongodb[database_name]
        collection = db[table_name]
        for page_num, page_data in pdfbody.items():
            collection.insert_one({
                "pdf_body": str(page_data),
                "file_name":  f"{str(metadata.get('filename'))}_{str(uuid4().hex)}",
                "made_on": str(datetime.utcnow()),
                "page_num": str(page_num)
            })
    except Exception as e:
        logging.error(f"[DB Ops - MongoDB] Error: {str(e)}")
        return False
    return True
