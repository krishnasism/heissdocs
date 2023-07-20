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


DOCUMENT_TABLE_KEYS = "file_name,page_num,made_on,s3_blob_file_name,s3_bucket_name"
SEARCH_KEY = "pdf_body"


def __search_elastic_search(
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
        documents: list = elasticsearch_client.search(
            index=settings.elastic_search_index, query=f"{query}", page_start=page_start
        )
        return documents
    except Exception as e:
        logging.error(f"[Elasticsearch] Error: {str(e)}")
        return []


def __search_document_db_mongodb(
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


def __search_document_db_aws(query: str, user_email: str, settings: Settings) -> list:
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


def get_pdf_by_query(query: str, user_email: str, page_start: int = 0) -> dict:
    """
    Get PDF by query from ElasticSearch and/or Document DB
    params: query: Query to search
    user_email: User email
    return: dict of list of documents
    """
    settings = override_settings(get_settings(), get_override_settings(user_email))
    documents: list = []
    if settings.search_document_db:
        match settings.no_sql_provider:
            case Databases.aws.value:
                documents.extend(__search_document_db_aws(query, user_email, settings))
            case Databases.mongodb.value:
                documents.extend(
                    __search_document_db_mongodb(query, user_email, settings)
                )
            case _:
                logging.error("[get_pdf_by_query] Undefined document database provider")
    if settings.search_elastic_search:
        documents.extend(
            __search_elastic_search(query, user_email, settings, page_start)
        )
    return {
        "documents": documents,
    }
