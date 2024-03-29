from boto3.dynamodb.conditions import Attr
import logging
from services.database.connectors import DatabaseConnection
from services.database.databases import Databases
from settings.config import get_settings, override_settings
from settings.override_config import get_override_settings
from settings.config import Settings
from services.elasticsearch.elasticsearch_client import ElasticSearchClient
from pymongo.collection import Collection
from pymongo import TEXT
from google.cloud.firestore import FieldFilter
from typing import Tuple

DOCUMENT_TABLE_KEYS = "file_name,page_num,made_on,blob_file_name,bucket_name"
DOCUMENT_TABLE_KEYS_WITH_UNIQUE_ID = (
    "unique_id,file_name,page_num,made_on,blob_file_name,bucket_name"
)
SEARCH_KEY = "pdf_body"


async def __search_elastic_search(
    query: str, user_email: str, settings: Settings, page_start: int = 0
) -> list:
    """
    Search ElasticSearch
    params: query: Query to search
    user_email: User email (unused)
    settings: Settings
    return list of documents
    """
    try:
        elasticsearch_client = ElasticSearchClient(
            host=settings.elastic_search_host, port=int(settings.elastic_search_port)
        )
        elasticsearch_client.connect(api_key=settings.elastic_search_api_key)
        documents: list = await elasticsearch_client.search(
            index=settings.elastic_search_index, query_str=query, page_start=page_start
        )
        return documents
    except Exception as e:
        logging.error(f"[Elasticsearch] Error: {str(e)}")
        return []


async def __search_document_db_mongodb(
    query: str, user_email: str, settings: Settings
) -> list:
    """
    Search Document DB in MongoDB
    params:
    query: Query to search
    user_email: User email (unused)
    settings: Settings
    return: list of documents
    """
    db_name = settings.mongo_db_database
    collection_name = settings.document_table_name
    try:
        mongodb_client = DatabaseConnection(
            settings.no_sql_provider, user_email
        ).db_client
        db = mongodb_client[db_name]
        collection: Collection = db[collection_name]
        collection.create_index([(SEARCH_KEY, TEXT)])
        search_query = {
            SEARCH_KEY: {
                "$regex": query,
                "$options": "i",
            },
        }
        # Project only the selected keys in the result
        select_keys = {key: 1 for key in DOCUMENT_TABLE_KEYS.split(",")}
        select_keys["_id"] = 0
        projection = select_keys
        documents = collection.find(search_query, projection)
        documents = list(documents)
    except Exception as e:
        logging.error(f"[MongoDBManager] Error: {str(e)}")
        logging.exception(e)
        return documents

    return documents


async def __search_document_db_aws(
    query: str, user_email: str, settings: Settings
) -> list:
    """
    Search Document DB in AWS
    params: query: Query to search
    user_email: User email (unused)
    settings: Settings
    return: list of documents
    """
    db_connection = DatabaseConnection(settings.no_sql_provider, user_email)
    select_keys = DOCUMENT_TABLE_KEYS
    table_name = settings.document_table_name
    search_key = SEARCH_KEY
    filter_expression = Attr(search_key).contains(query)
    dynamodb = db_connection.db_client
    try:
        if table_name:
            table = dynamodb.Table(table_name)
            response = table.scan(
                FilterExpression=filter_expression, ProjectionExpression=select_keys
            )
            documents: list = response["Items"]
            while "LastEvaluatedKey" in response:
                response = table.scan(
                    ExclusiveStartKey=response["LastEvaluatedKey"],
                    FilterExpression=filter_expression,
                    ProjectionExpression=select_keys,
                )
                documents.extend(response.get("Items"))
        else:
            raise Exception("No table name was defined")
    except Exception as e:
        logging.error(f"[AWSManager] Error: {str(e)}")
        return []
    return documents


async def __search_document_db_gcp_firestore(
    query: str, user_email: str, settings: Settings
):
    db_connection = DatabaseConnection(settings.no_sql_provider, user_email)
    firestore = db_connection.db_client
    try:
        collection_name = settings.document_table_name
        collection_ref = firestore.collection(collection_name)

        query_obj = collection_ref.where(
            filter=FieldFilter(SEARCH_KEY, ">=", query)
        ).where(filter=FieldFilter(SEARCH_KEY, "<=", query + "\uf8ff"))
        query_obj = query_obj.select(DOCUMENT_TABLE_KEYS.split(","))
        documents = query_obj.stream()
        results = [doc.to_dict() for doc in documents]
    except Exception as e:
        logging.error(f"[GCP Firestore] Error: {str(e)}")
        logging.exception(e)
        return []
    return results


async def __search_document_db_azure_cosmosdb(
    query: str, user_email: str, settings: Settings
):
    db_connection = DatabaseConnection(settings.no_sql_provider, user_email)
    cosmosdb = db_connection.db_client
    database = cosmosdb.get_database_client(settings.cosmos_db_database)
    container = database.get_container_client(settings.document_table_name)
    query = query.replace(" ", "\n")
    query_string = f"""
        SELECT *
        FROM {settings.document_table_name} c
        WHERE CONTAINS(c.{SEARCH_KEY}, "{query}")
    """
    try:
        documents = container.query_items(
            query=query_string,
            enable_cross_partition_query=True,
        )
        results = [doc for doc in documents]
    except Exception as e:
        logging.error(f"[Azure CosmosDB] Error: {str(e)}")
        logging.exception(e)
        return []
    return results


async def get_pdf_by_query(
    query: str, user_email: str, page_start: int = 0
) -> list[dict]:
    """
    Get PDF by query from ElasticSearch and/or Document DB
    params: query: Query to search
    user_email: User email
    return: dict of list of documents
    """
    settings = override_settings(get_settings(), get_override_settings(user_email))
    documents: list = []
    response_documents: list = []
    if settings.search_document_db:
        match settings.no_sql_provider:
            case Databases.aws.value:
                response_documents = await __search_document_db_aws(
                    query, user_email, settings
                )
            case Databases.mongodb.value:
                response_documents = await __search_document_db_mongodb(
                    query, user_email, settings
                )
            case Databases.gcp.value:
                response_documents = await __search_document_db_gcp_firestore(
                    query, user_email, settings
                )
            case Databases.azure.value:
                response_documents = await __search_document_db_azure_cosmosdb(
                    query, user_email, settings
                )
            case _:
                logging.error("[get_pdf_by_query] Undefined document database provider")
        if response_documents:
            documents.extend(response_documents)
    if settings.search_elastic_search:
        documents.extend(
            await __search_elastic_search(query, user_email, settings, page_start)
        )
    return {
        "documents": documents,
    }


async def __get_all_documents_aws(
    user_email: str, settings: Settings
) -> Tuple[list, str]:
    """
    Retrieve all documents from AWS Document DB
    settings: Settings
    return: list of documents
    """
    db_connection = DatabaseConnection(settings.no_sql_provider, user_email=None)
    select_keys = DOCUMENT_TABLE_KEYS_WITH_UNIQUE_ID
    table_name = settings.document_table_name
    dynamodb = db_connection.db_client
    try:
        if table_name:
            table = dynamodb.Table(table_name)
            response = table.scan(ProjectionExpression=select_keys)
            documents: list = response["Items"]
            while "LastEvaluatedKey" in response:
                response = table.scan(
                    ExclusiveStartKey=response["LastEvaluatedKey"],
                    ProjectionExpression=select_keys,
                )
                documents.extend(response.get("Items"))
        else:
            raise Exception("No table name was defined")
    except Exception as e:
        logging.error(f"[AWSManager] Error: {str(e)}")
        return [], str(e)
    return documents, None


async def __get_all_documents_firestore(
    user_email: str, settings: Settings
) -> Tuple[list, str]:
    """
    Retrieve all documents from GCP Firestore
    settings: Settings
    return: list of documents
    """
    db_connection = DatabaseConnection(settings.no_sql_provider, user_email=None)
    firestore = db_connection.db_client
    try:
        collection_name = settings.document_table_name
        collection_ref = firestore.collection(collection_name)
        query_obj = collection_ref.select(DOCUMENT_TABLE_KEYS_WITH_UNIQUE_ID.split(","))
        documents = query_obj.stream()
        results = [doc.to_dict() for doc in documents]
    except Exception as e:
        logging.error(f"[GCP Firestore] Error: {str(e)}")
        logging.exception(e)
        return [], str(e)
    return results, None


async def __get_all_documents_cosmosdb(
    user_email: str, settings: Settings
) -> Tuple[list, str]:
    """
    Retrieve all documents from Azure CosmosDB
    settings: Settings
    return: list of documents
    """
    db_connection = DatabaseConnection(settings.no_sql_provider, user_email=None)
    cosmosdb = db_connection.db_client
    database = cosmosdb.get_database_client(settings.cosmos_db_database)
    container = database.get_container_client(settings.document_table_name)
    query_string = f"SELECT * FROM {settings.document_table_name}"
    try:
        documents = container.query_items(
            query=query_string, enable_cross_partition_query=True
        )
        results = [doc for doc in documents]
    except Exception as e:
        logging.error(f"[Azure CosmosDB] Error: {str(e)}")
        logging.exception(e)
        return [], str(e)
    return results, None


async def __get_all_documents_mongodb(
    user_email: str, settings: Settings
) -> Tuple[list, str]:
    """
    Retrieve all documents from MongoDB
    settings: Settings
    return: list of documents
    """
    db_name = settings.mongo_db_database
    collection_name = settings.document_table_name
    try:
        mongodb_client = DatabaseConnection(
            settings.no_sql_provider, user_email=None
        ).db_client
        db = mongodb_client[db_name]
        collection: Collection = db[collection_name]
        # Project only the selected keys in the result
        select_keys = {key: 1 for key in DOCUMENT_TABLE_KEYS_WITH_UNIQUE_ID.split(",")}
        select_keys["_id"] = 0
        projection = select_keys
        documents = collection.find({}, projection)
        documents = list(documents)
    except Exception as e:
        logging.error(f"[MongoDBManager] Error: {str(e)}")
        logging.exception(e)
        return [], str(e)

    return documents, None


async def get_all_document_db_docs(user_email: str) -> dict:
    settings = override_settings(get_settings(), get_override_settings(user_email))
    documents: list = []
    error = None

    response_documents: list = []
    match settings.no_sql_provider:
        case Databases.aws.value:
            response_documents, error = await __get_all_documents_aws(
                user_email, settings
            )
        case Databases.mongodb.value:
            response_documents, error = await __get_all_documents_mongodb(
                user_email, settings
            )
        case Databases.gcp.value:
            response_documents, error = await __get_all_documents_firestore(
                user_email, settings
            )
        case Databases.azure.value:
            response_documents, error = await __get_all_documents_cosmosdb(
                user_email, settings
            )
        case _:
            logging.error("[get_all_documents] Undefined document database provider")
    if response_documents:
        documents.extend(response_documents)

    return {
        "documents": documents,
        "error": error,
    }


async def __delete_document_aws(
    unique_id: str, user_email: str, settings: Settings
) -> str:
    db_connection = DatabaseConnection(settings.no_sql_provider, user_email=user_email)
    table_name = settings.document_table_name
    dynamodb = db_connection.db_client
    try:
        if table_name:
            table = dynamodb.Table(table_name)
            response = table.delete_item(Key={"unique_id": unique_id})
        else:
            raise Exception("No table name was defined")
    except Exception as e:
        logging.error(f"[AWSManager] Delete Error: {str(e)}")
        return str(e)
    return "deleted"


async def __delete_document_firestore(
    unique_id: str, user_email: str, settings: Settings
) -> str:
    db_connection = DatabaseConnection(settings.no_sql_provider, user_email=user_email)
    firestore = db_connection.db_client
    try:
        collection_name = settings.document_table_name
        collection_ref = firestore.collection(collection_name)
        document_ref = collection_ref.document(unique_id)
        document_ref.delete()
    except Exception as e:
        logging.error(f"[GCP Firestore] Delete Error: {str(e)}")
        return str(e)
    return "deleted"


async def __delete_document_cosmosdb(
    unique_id: str, cosmos_id: str, user_email: str, settings: Settings
) -> str:
    db_connection = DatabaseConnection(settings.no_sql_provider, user_email=user_email)
    cosmosdb = db_connection.db_client
    database = cosmosdb.get_database_client(settings.cosmos_db_database)
    container = database.get_container_client(settings.document_table_name)
    try:
        response = container.delete_item(item=cosmos_id, partition_key=unique_id)
    except Exception as e:
        logging.error(f"[Azure CosmosDB] Delete Error: {str(e)}")
        return str(e)
    return "deleted"


async def __delete_document_mongodb(
    unique_id: str, user_email: str, settings: Settings
) -> str:
    db_name = settings.mongo_db_database
    collection_name = settings.document_table_name
    try:
        mongodb_client = DatabaseConnection(
            settings.no_sql_provider, user_email=user_email
        ).db_client
        db = mongodb_client[db_name]
        collection: Collection = db[collection_name]
        result = collection.delete_one({"unique_id": unique_id})
        if result.deleted_count == 0:
            raise Exception("Document not found")
    except Exception as e:
        logging.error(f"[MongoDBManager] Delete Error: {str(e)}")
        return str(e)
    return "deleted"


async def delete_document_from_document_db(
    user_email: str, unique_id: str, cosmos_id: str
) -> str:
    settings = override_settings(get_settings(), get_override_settings(user_email))
    match settings.no_sql_provider:
        case Databases.aws.value:
            response = await __delete_document_aws(unique_id, user_email, settings)
        case Databases.mongodb.value:
            response = await __delete_document_mongodb(unique_id, user_email, settings)
        case Databases.gcp.value:
            response = await __delete_document_firestore(
                unique_id, user_email, settings
            )
        case Databases.azure.value:
            response = await __delete_document_cosmosdb(
                unique_id, user_email, cosmos_id, settings
            )
        case _:
            logging.error("[get_all_documents] Undefined document database provider")

    return {
        "success": response == "deleted",
        "error": response if response != "deleted" else None,
    }
