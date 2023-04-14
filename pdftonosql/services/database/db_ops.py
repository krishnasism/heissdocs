from .connectors import DatabaseConnection
from .databases import Databases
from datetime import datetime
from uuid import uuid4
import logging

CONFIGURED_DB = Databases.aws.value  # TODO: This needs to come from config
TABLE_NAME = "documents"  # TODO: Needs to come from config


def put_pdf_to_database(pdf_body, file_metadata, table_name):
    database_connection = DatabaseConnection(CONFIGURED_DB)
    match CONFIGURED_DB:
        case Databases.mongodb.value:
            pass
        case Databases.aws.value:
            return _put_pdf_body_dynamodb(database_connection.db_client, pdf_body, file_metadata, table_name)
        case _:
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
