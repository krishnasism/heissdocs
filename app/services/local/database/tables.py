from sqlalchemy import String, Numeric, Boolean, DateTime
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
settings_table = sa.Table(
    "settings",
    Base.metadata,
    sa.Column("id", String),
    sa.Column("user_email", String),
    sa.Column("aws_access_key", String),
    sa.Column("aws_secret", String),
    sa.Column("aws_region", String),
    sa.Column("no_sql_provider", String),
    sa.Column("document_table_name", String),
    sa.Column("parsing_api_key", String),
    sa.Column("buckets_list", String),
    sa.Column("scan_bucket", String),
    sa.Column("elastic_search_index", String),
    sa.Column("elastic_search_host", String),
    sa.Column("elastic_search_port", String),
    sa.Column("elastic_search_api_key", String),
    sa.Column("search_document_db", Boolean),
    sa.Column("search_elastic_search", Boolean),
    sa.Column("store_logs_in_db", Boolean),
    sa.Column("mongo_db_database", String),
    sa.Column("mongo_db_username", String),
    sa.Column("mongo_db_password", String),
    sa.Column("mongo_db_host", String),
    sa.Column("openai_api_key", String),
    sa.Column("qdrant_host", String),
    sa.Column("qdrant_collection_name", String),
    sa.Column("qdrant_port", String),
    sa.Column("qdrant_api_key", String),
    sa.Column("hugging_face_api_key", String),
    sa.Column("cloud_provider", String),
    sa.Column("azure_blob_connection_string", String),
    sa.Column("azure_blob_container_name", String),
    sa.Column("cosmos_db_host", String),
    sa.Column("cosmos_db_container", String),
    sa.Column("cosmos_db_key", String),
    sa.Column("gcp_key_file_content", String),
)


documents_progress_table = sa.Table(
    "documents_progress",
    Base.metadata,
    sa.Column("id", String),
    sa.Column("user_email", String),
    sa.Column("document_id", String),
    sa.Column("document_name", String),
    sa.Column("stage", String),
    sa.Column("pages_parsed", Numeric),
    sa.Column("total_pages", Numeric),
    sa.Column("updated_on", DateTime),
)

logs_table = sa.Table(
    "logs",
    Base.metadata,
    sa.Column("log_id", String),
    sa.Column("user_email", String),
    sa.Column("log_level", String),
    sa.Column("message", String),
    sa.Column("created_on", DateTime),
    sa.Column("caller_filename", String),
    sa.Column("caller_function_name", String),
    sa.Column("caller_line_number", String),
)

# TODO : Add auto migrations from tables -> database
