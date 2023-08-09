from pydantic import BaseSettings
from functools import lru_cache
from typing import Optional


class Settings(BaseSettings):
    aws_access_key: str
    aws_secret: str
    aws_region: str
    document_table_name: str
    cloud_provider: str
    document_db: str
    no_sql_provider: str
    postgres_username: str
    postgres_password: str
    postgres_endpoint: str
    auth0_domain: str
    auth0_api_audience: str
    auth0_algorithms: str
    auth0_issuer: str
    auth0_client_id: str
    auth0_client_secret: str
    parsing_queue_endpoint: str
    parsing_queue_name: str
    temp_storage_endpoint: str
    temp_storage_bucket_name: str
    minio_access_key: str
    minio_secret_key: str
    minio_endpoint: str
    minio_secure: str
    elastic_search_index: str
    elastic_search_host: str
    elastic_search_port: int
    elastic_search_api_key: str
    search_elastic_search: Optional[bool] = False
    search_document_db: Optional[bool] = False
    store_logs_in_db: Optional[bool] = False
    mongo_db_database: str
    mongo_db_host: str
    mongo_db_username: str
    mongo_db_password: str
    openai_api_key: str
    huggingfacehub_api_key: str
    qdrant_api_key: str
    qdrant_host: str
    qdrant_port: int
    qdrant_collection_name: str

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()


def override_settings(settings: Settings, override_settings_dict: dict) -> Settings:
    for key, value in override_settings_dict.items():
        if hasattr(settings, key):
            setattr(settings, key, value)
    return settings
