import logging
from settings.config import get_settings, override_settings
from settings.override_config import get_override_settings
from services.elasticsearch.elasticsearch_client import ElasticSearchClient
from typing import Tuple


async def fetch_scroll_elasticsearch_files(
    user_email: str, scroll_id: str = None
) -> Tuple[list, str, str]:
    settings = override_settings(get_settings(), get_override_settings(user_email))
    try:
        selected_fields = [
            "file_name",
            "page_num",
            "made_on",
            "blob_file_name",
            "bucket_name",
        ]
        elasticsearch_client = ElasticSearchClient(
            host=settings.elastic_search_host, port=int(settings.elastic_search_port)
        )
        elasticsearch_client.connect(api_key=settings.elastic_search_api_key)
        all_documents, scroll_id, error = await elasticsearch_client.scroll(
            index=settings.elastic_search_index,
            scroll_id=scroll_id,
            selected_fields=selected_fields,
            scroll_time="3m",
        )
        return all_documents, scroll_id, error
    except Exception as e:
        logging.error(f"[Elasticsearch] Error: {str(e)}")
        return [], "", str(e)


async def remove_elasticsearch_file(user_email: str, file_id: str) -> bool:
    settings = override_settings(get_settings(), get_override_settings(user_email))
    try:
        elasticsearch_client = ElasticSearchClient(
            host=settings.elastic_search_host, port=int(settings.elastic_search_port)
        )
        elasticsearch_client.connect(api_key=settings.elastic_search_api_key)
        return await elasticsearch_client.delete(
            index=settings.elastic_search_index,
            file_id=file_id,
        )
    except Exception as e:
        logging.error(f"[Elasticsearch] Error: {str(e)}")
        return False
