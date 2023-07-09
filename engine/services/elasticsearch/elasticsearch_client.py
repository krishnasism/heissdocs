from elasticsearch import Elasticsearch
from services.settings.settings import Settings
import logging


class ElasticSearchClient:
    def __init__(self, host: str, port: str):
        self.host = host
        self.port = port
        if self.host.startswith("https://"):
            self.scheme = "https"
        else:
            self.scheme = "http"
        self.client = None

    def connect(self, api_key: str = None):
        try:
            if api_key:
                self.client = Elasticsearch(
                    [{"host": self.host, "port": self.port, "scheme": self.scheme}],
                    api_key=api_key,
                )
            else:
                self.client = Elasticsearch(
                    [{"host": self.host, "port": self.port, "scheme": self.scheme}]
                )
            logging.info("[ElasticSearchClient] Connected to ElasticSearch")
        except Exception as e:
            logging.exception(f"[ElasticSearchClient - Connect] {e}")

    def insert_document_to_index(self, index: str, document: dict):
        try:
            self.client.index(index=index, document=document)
            logging.info(f"[ElasticSearchClient] Inserted document to {index}")
        except Exception as e:
            logging.exception(f"[ElasticSearchClient] {e}")


def insert_document_to_elasticsearch(document: dict, file_metadata: dict):
    settings = Settings.get_settings()
    try:
        elasticsearch_client = ElasticSearchClient(
            host=settings.elastic_search_host, port=int(settings.elastic_search_port)
        )
        elasticsearch_client.connect(api_key=settings.elastic_search_api_key)
        for page_num, page_data in document.items():
            document = {
                "pdf_body": str(page_data),
                "file_name": file_metadata.get("filename"),
                "made_on": str(file_metadata.get("made_on")),
                "page_num": str(page_num),
                "s3_blob_file_name": str(file_metadata.get("s3_blob_file_name", "")),
                "s3_bucket_name": str(file_metadata.get("s3_bucket_name", "")),
            }
            elasticsearch_client.insert_document_to_index(
                index=settings.elastic_search_index, document=document
            )
        logging.info("[Elasticsearch] Inserted document to Elasticsearch")
        return True
    except Exception as e:
        logging.error(f"[Elasticsearch] {e}")
        return False
