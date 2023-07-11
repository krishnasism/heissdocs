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
    sa.Column("updated_on", DateTime)
)

# TODO : Add auto migrations from tables -> database
