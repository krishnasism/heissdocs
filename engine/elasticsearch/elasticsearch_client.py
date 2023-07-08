from elasticsearch import Elasticsearch
import logging


class ElasticSearchClient:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.client = None

    def connect(self, api_key: str = None):
        try:
            if api_key:
                self.client = Elasticsearch(
                    [{"host": self.host, "port": self.port}], api_key=api_key
                )
            else:
                self.client = Elasticsearch([{"host": self.host, "port": self.port}])
            logging.info("[ElasticSearchClient] Connected to ElasticSearch")
        except Exception as e:
            logging.error(f"[ElasticSearchClient] {e}")

    def insert_document_to_index(self, index: str, document: dict):
        try:
            self.client.index(index=index, body=document)
            logging.info(f"[ElasticSearchClient] Inserted document to {index}")
        except Exception as e:
            logging.error(f"[ElasticSearchClient] {e}")
