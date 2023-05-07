from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    aws_access_key: str
    aws_secret: str
    aws_region: str
    aws_search_table_name: str
    cloud_provider: str
    document_db: str
    document_db_provider: str
    mongodb_db_name: str
    mongodb_collection_name: str
    mongodb_db_endpoint: str
    mongodb_db_username: str
    mongodb_db_password: str
    postgres_username: str
    postgres_password:  str
    postgres_endpoint: str
    auth0_domain: str
    auth0_api_audience: str
    auth0_algorithms: str
    auth0_issuer: str
    auth0_client_id: str
    auth0_client_secret: str

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
