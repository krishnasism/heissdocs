"""init

Revision ID: 4e98f13d1b1d
Revises: 
Create Date: 2023-09-05 22:30:15.671991

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4e98f13d1b1d"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "documents_progress",
        sa.Column("id", sa.String(), nullable=True),
        sa.Column("user_email", sa.String(), nullable=True),
        sa.Column("document_id", sa.String(), nullable=True),
        sa.Column("document_name", sa.String(), nullable=True),
        sa.Column("stage", sa.String(), nullable=True),
        sa.Column("pages_parsed", sa.Integer(), nullable=True),
        sa.Column("total_pages", sa.Integer(), nullable=True),
        sa.Column("updated_on", sa.DateTime(), nullable=True),
    )
    op.create_table(
        "logs",
        sa.Column("log_id", sa.String(), nullable=True),
        sa.Column("user_email", sa.String(), nullable=True),
        sa.Column("log_level", sa.String(), nullable=True),
        sa.Column("message", sa.String(), nullable=True),
        sa.Column("created_on", sa.DateTime(), nullable=True),
        sa.Column("caller_filename", sa.String(), nullable=True),
        sa.Column("caller_function_name", sa.String(), nullable=True),
        sa.Column("caller_line_number", sa.String(), nullable=True),
    )
    op.create_table(
        "settings",
        sa.Column("id", sa.String(), nullable=True),
        sa.Column("user_email", sa.String(), nullable=True),
        sa.Column("aws_access_key", sa.String(), nullable=True),
        sa.Column("aws_secret", sa.String(), nullable=True),
        sa.Column("aws_region", sa.String(), nullable=True),
        sa.Column("no_sql_provider", sa.String(), nullable=True),
        sa.Column("document_table_name", sa.String(), nullable=True),
        sa.Column("parsing_api_key", sa.String(), nullable=True),
        sa.Column("buckets_list", sa.String(), nullable=True),
        sa.Column("scan_bucket", sa.String(), nullable=True),
        sa.Column("elastic_search_index", sa.String(), nullable=True),
        sa.Column("elastic_search_host", sa.String(), nullable=True),
        sa.Column("elastic_search_port", sa.String(), nullable=True),
        sa.Column("elastic_search_api_key", sa.String(), nullable=True),
        sa.Column("search_document_db", sa.Boolean(), nullable=True),
        sa.Column("search_elastic_search", sa.Boolean(), nullable=True),
        sa.Column("store_logs_in_db", sa.Boolean(), nullable=True),
        sa.Column("mongo_db_database", sa.String(), nullable=True),
        sa.Column("mongo_db_username", sa.String(), nullable=True),
        sa.Column("mongo_db_password", sa.String(), nullable=True),
        sa.Column("mongo_db_host", sa.String(), nullable=True),
        sa.Column("openai_api_key", sa.String(), nullable=True),
        sa.Column("qdrant_host", sa.String(), nullable=True),
        sa.Column("qdrant_collection_name", sa.String(), nullable=True),
        sa.Column("qdrant_port", sa.String(), nullable=True),
        sa.Column("qdrant_api_key", sa.String(), nullable=True),
        sa.Column("hugging_face_api_key", sa.String(), nullable=True),
        sa.Column("cloud_provider", sa.String(), nullable=True),
        sa.Column("azure_blob_connection_string", sa.String(), nullable=True),
        sa.Column("cosmos_db_host", sa.String(), nullable=True),
        sa.Column("cosmos_db_container", sa.String(), nullable=True),
        sa.Column("cosmos_db_database", sa.String(), nullable=True),
        sa.Column("cosmos_db_key", sa.String(), nullable=True),
        sa.Column("gcp_key_file_content", sa.String(), nullable=True),
        sa.Column("open_ai_type", sa.String(), nullable=True),
        sa.Column("open_ai_base", sa.String(), nullable=True),
        sa.Column("open_ai_deployment_name", sa.String(), nullable=True),
        sa.Column("open_ai_api_version", sa.String(), nullable=True),
        sa.Column("open_ai_model_name", sa.String(), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("settings")
    op.drop_table("logs")
    op.drop_table("documents_progress")
    # ### end Alembic commands ###
