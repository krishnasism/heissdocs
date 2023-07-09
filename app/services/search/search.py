from boto3.dynamodb.conditions import Attr
import logging
from services.database.connectors import DatabaseConnection
from services.database.databases import Databases
from settings.config import get_settings, override_settings
from settings.override_config import get_override_settings
from settings.config import Settings
from services.elasticsearch.elasticsearch_client import ElasticSearchClient

DOCUMENT_TABLE_KEYS = "file_name,page_num,made_on,s3_blob_file_name,s3_bucket_name"
SEARCH_KEY = "pdf_body"


def __search_elastic_search(query, user_email, settings: Settings) -> list:
    try:
        elasticsearch_client = ElasticSearchClient(
            host=settings.elastic_search_host, port=int(settings.elastic_search_port)
        )
        elasticsearch_client.connect(api_key=settings.elastic_search_api_key)
        documents: list = elasticsearch_client.search(
            index=settings.elastic_search_index, query=query
        )
        return documents
    except Exception as e:
        logging.error(f"[AWSManager] Error: {str(e)}")
        return []


def __search_document_db(query, user_email, settings: Settings) -> list:
    db_connection = DatabaseConnection(settings.document_db_provider, user_email)
    select_keys = DOCUMENT_TABLE_KEYS
    table_name = settings.aws_search_table_name
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


def get_pdf_by_query(query, user_email):
    settings = override_settings(get_settings(), get_override_settings(user_email))
    documents: list = []
    # TODO: Only works with dynamodb now - Implement generic
    if settings.document_db_provider != Databases.aws.value:
        return []
    if settings.search_document_db:
        documents.extend(__search_document_db(query, user_email, settings))
    if settings.search_elastic_search:
        documents.extend(__search_elastic_search(query, user_email, settings))
    return {
        "documents": documents,
    }
