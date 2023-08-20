from .connectors import DatabaseConnection
from services.settings.settings import Settings
from .databases import Databases
from datetime import datetime
from uuid import uuid4
import logging


def put_pdf_to_document_db(pdf_body: dict, file_metadata: dict) -> None:
    """
    Put text from parsed PDF to Document DB
    params: pdf_body: PDF body
    file_metadata: File metadata
    return: None
    """
    _settings = Settings.get_settings()
    configured_db = _settings.no_sql_provider
    database_connection = DatabaseConnection(configured_db)
    match configured_db:
        case Databases.mongodb.value:
            return __put_pdf_body_mongodb(
                database_connection.db_client,
                pdf_body,
                file_metadata,
                database_name=_settings.mongo_db_database,
                table_name=_settings.document_table_name,
            )
        case Databases.aws.value:
            return __put_pdf_body_dynamodb(
                database_connection.db_client,
                pdf_body,
                file_metadata,
                table_name=_settings.document_table_name,
            )
        case Databases.gcp.value:
            return __put_pdf_body_gcp(
                database_connection.db_client,
                pdf_body,
                file_metadata,
                table_name=_settings.document_table_name,
            )
        case Databases.azure.value:
            return __put_pdf_body_azure(
                database_connection.db_client,
                pdf_body,
                file_metadata,
                table_name=_settings.document_table_name,
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
                    "blob_file_name": str(metadata.get("blob_file_name", "")),
                    "bucket_name": str(metadata.get("bucket_name", "")),
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
    """
    Put PDF body to MongoDB
    """
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
                    "blob_file_name": str(metadata.get("blob_file_name", "")),
                    "bucket_name": str(metadata.get("bucket_name", "")),
                }
            )
    except Exception as e:
        logging.error(f"[DB Ops - MongoDB] Error: {e}")
        return False
    return True


def __put_pdf_body_gcp(firestore, pdfbody, metadata, table_name):
    """
    Put PDF body to GCP Firestore
    """
    try:
        collection_ref = firestore.collection(table_name)

        for page_num, page_data in pdfbody.items():
            document_data = {
                "pdf_body": str(page_data),
                "file_name": metadata.get("filename"),
                "made_on": str(datetime.utcnow()),
                "page_num": str(page_num),
                "blob_file_name": str(metadata.get("blob_file_name", "")),
                "bucket_name": str(metadata.get("bucket_name", "")),
            }
            document_ref = collection_ref.document()
            document_ref.set(document_data)

    except Exception as e:
        logging.error(
            f"[DB Ops - Firestore] Unable to put pdf body into {table_name} collection"
        )
        logging.exception(e)
        return False
    return True


def __put_pdf_body_azure(cosmosdb, pdfbody, metadata, table_name):
    _settings = Settings.get_settings()
    """
    Put PDF body to Azure CosmosDB
    """
    try:
        database = cosmosdb.get_database_client(_settings.cosmos_db_database)
        container = database.get_container_client(table_name)
        for page_num, page_data in pdfbody.items():
            item = {
                "id": str(uuid4()),
                "pdf_body": str(page_data),
                "file_name": metadata.get("filename"),
                "made_on": str(datetime.utcnow()),
                "page_num": str(page_num),
                "blob_file_name": str(metadata.get("blob_file_name", "")),
                "bucket_name": str(metadata.get("bucket_name", "")),
            }
            container.upsert_item(item)
    except Exception as e:
        logging.error(
            f"[DB Ops - CosmosDB] Unable to put pdf body into {table_name} table"
        )
        logging.exception(e)
        return False
    return True
