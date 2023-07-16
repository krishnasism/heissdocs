from .connectors import DatabaseConnection
from services.settings.settings import Settings
from .databases import Databases
from datetime import datetime
from uuid import uuid4
import logging


def put_pdf_to_document_db(pdf_body: str, file_metadata: dict) -> None:
    """
    Put text from parsed PDF to Document DB
    params: pdf_body: PDF body
    file_metadata: File metadata
    return: None
    """
    _settings = Settings.get_settings()
    configured_db = _settings.document_db_provider
    database_connection = DatabaseConnection(configured_db)
    match configured_db:
        case Databases.mongodb.value:
            return __put_pdf_body_mongodb(
                database_connection.db_client,
                pdf_body,
                file_metadata,
                database_name=_settings.mongodb_db_name,
                table_name=_settings.mongodb_collection_name,
            )
        case Databases.aws.value:
            return __put_pdf_body_dynamodb(
                database_connection.db_client,
                pdf_body,
                file_metadata,
                table_name=_settings.aws_search_table_name,
            )
        case _:
            logging.error(
                f"[DB Ops - Document DB] Undefined provider. Provider: {configured_db}"
            )
            pass


def __put_pdf_body_dynamodb(dynamodb, pdfbody, metadata, table_name):
    try:
        table = dynamodb.Table(table_name)
        for page_num, page_data in pdfbody.items():
            table.put_item(
                Item={
                    "pdf_body": str(page_data),
                    "file_name": metadata.get("filename"),
                    "made_on": str(datetime.utcnow()),
                    "page_num": str(page_num),
                    "s3_blob_file_name": str(metadata.get("s3_blob_file_name", "")),
                    "s3_bucket_name": str(metadata.get("s3_bucket_name", "")),
                }
            )
    except Exception as e:
        logging.error(
            f"[DB Ops - DynamoDB] Unable to put pdf body into {table_name} table"
        )
        logging.exception(e)
        return False
    return True


def __put_pdf_body_mongodb(mongodb, pdfbody, metadata, database_name, table_name):
    """Unimplemented"""
    try:
        db = mongodb[database_name]
        collection = db[table_name]
        for page_num, page_data in pdfbody.items():
            collection.insert_one(
                {
                    "pdf_body": str(page_data),
                    "file_name": f"{str(metadata.get('filename'))}_{str(uuid4().hex)}",
                    "made_on": str(datetime.utcnow()),
                    "page_num": str(page_num),
                }
            )
    except Exception as e:
        logging.error(f"[DB Ops - MongoDB] Error: {e}")
        return False
    return True
