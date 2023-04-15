from boto3.dynamodb.conditions import Attr, Key
import logging
from services.database.connectors import DatabaseConnection
from services.database.databases import Databases

# TODO: Config

DOCUMENT_TABLE_KEYS = "file_name,page_num"
DOCUMENT_TABLE = "documents"
SEARCH_KEY = "pdf_body"

####


def get_pdf_by_query(query):
    db_connection = DatabaseConnection(Databases.aws.value)
    select_keys = DOCUMENT_TABLE_KEYS
    dynamodb = db_connection.db_client
    table_name = DOCUMENT_TABLE
    search_key = SEARCH_KEY
    filter_expression = Attr(search_key).contains(query)
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
