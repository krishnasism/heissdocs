from boto3.dynamodb.conditions import Attr
import logging
from services.database.connectors import DatabaseConnection
from services.database.databases import Databases
import os

# TODO: Config
DOCUMENT_DB_PROVIDER = os.getenv("DOCUMENT_DB_PROVIDER")
AWS_SEARCH_TABLE_NAME = os.getenv("AWS_SEARCH_TABLE_NAME")

DOCUMENT_TABLE_KEYS = "file_name,page_num"
SEARCH_KEY = "pdf_body"


def get_pdf_by_query(query):
    # TODO: Only works with dynamodb now - Implement generic
    if DOCUMENT_DB_PROVIDER != Databases.aws.value:
        return []

    db_connection = DatabaseConnection(DOCUMENT_DB_PROVIDER)
    select_keys = DOCUMENT_TABLE_KEYS
    table_name = AWS_SEARCH_TABLE_NAME
    search_key = SEARCH_KEY
    filter_expression = Attr(search_key).contains(query)
    dynamodb = db_connection.db_client
    try:
        if table_name:
            table = dynamodb.Table(table_name)
            response = table.scan(
                FilterExpression=filter_expression,
                ProjectionExpression=select_keys
            )
            documents = response['Items']
            while 'LastEvaluatedKey' in response:
                response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'],
                                      FilterExpression=filter_expression,
                                      ProjectionExpression=select_keys)
            documents.extend(response.get('Items'))
        else:
            raise Exception("No table name was defined")
    except Exception as e:
        logging.error(f"[AWSManager] Error: {str(e)}")
        return None
    return documents
