from boto3.dynamodb.conditions import Attr
import logging
from services.database.connectors import DatabaseConnection
from services.database.databases import Databases
from settings.config import get_settings, override_settings
from settings.override_config import get_override_settings

DOCUMENT_TABLE_KEYS = "file_name,page_num,made_on,s3_blob_file_name,s3_bucket_name"
SEARCH_KEY = "pdf_body"


def get_pdf_by_query(query, user_email):
    settings = override_settings(get_settings(), get_override_settings(user_email))
    # TODO: Only works with dynamodb now - Implement generic
    if settings.document_db_provider != Databases.aws.value:
        return []

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
            documents = response["Items"]
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
        return {
            "error": str(e)
        }
    return {
        "documents": documents
    }
