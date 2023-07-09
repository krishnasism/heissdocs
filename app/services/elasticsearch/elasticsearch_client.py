from elasticsearch import Elasticsearch
import logging


class ElasticSearchClient:
    def __init__(self, host: str, port: int):
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
            logging.error(f"[ElasticSearchClient] {e}")

    def search(self, index: str, query: str):
        query = {"query": {"match": {"pdf_body": {"query": query.lower()}}}}
        try:
            elastic_response = self.client.search(index=index, body=query)
            elastic_response = elastic_response.get("hits", {}).get("hits", [])
            return [hit["_source"] for hit in elastic_response]
        except Exception as e:
            logging.error(f"[ElasticSearchClient] {e}")
