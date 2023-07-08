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

    def search(self, index: str, query: str):
        try:
            return self.client.search(index=index, body=query)
        except Exception as e:
            logging.error(f"[ElasticSearchClient] {e}")
