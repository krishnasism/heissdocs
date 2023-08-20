from elasticsearch import Elasticsearch
import logging
from typing import Tuple


class ElasticSearchClient:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        if self.host.startswith("https://"):
            self.scheme = "https"
            self.host = self.host.replace("https://", "")
        else:
            self.scheme = "http"
            self.host = self.host.replace("http://", "")

        self.client = None

    def connect(self, api_key: str = None):
        """
        Connect to ElasticSearch
        params: api_key: API Key for ElasticSearch (not required for localhost)
        return: None
        """
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

    async def search(
        self,
        index: str,
        query_str: str,
        page_start: int = 0,
        page_size: int = 10,
    ):
        """
        Search ElasticSearch
        params: index: ElasticSearch index to search
        params: query_str: Query to search
        params: page_start: Page start for pagination
        params: page_size: Page size for pagination
        return: List of documents
        """
        query = {
            "from": page_start,
            "size": page_size,
            "sort": ["_score"],
            "query": {
                "match": {
                    "pdf_body": {
                        "query": f"*{query_str.lower()}*",
                    }
                }
            },
        }
        try:
            elastic_response = self.client.search(index=index, body=query)
            elastic_response = elastic_response.get("hits", {}).get("hits", [])

            return [hit["_source"] for hit in elastic_response]
        except Exception as e:
            logging.error(f"[ElasticSearchClient] {e}")

    async def scroll(
        self,
        index: str,
        scroll_id: str = None,
        selected_fields: list = [],
        scroll_time: str = "3m",
    ) -> Tuple[dict, str]:
        """
        Scroll ElasticSearch
        params: index: ElasticSearch index to search
        params: query_str: Query to search
        params: page_start: Page start for pagination
        params: page_size: Page size for pagination
        return: List of documents
        """
        query = {
            "size": 1000,
            "query": {"match_all": {}},
        }
        if selected_fields:
            query["_source"] = selected_fields
        try:
            if not scroll_id:
                elastic_response = self.client.search(
                    index=index, body=query, scroll=scroll_time
                )
                scroll_id = elastic_response["_scroll_id"]
            else:
                elastic_response = self.client.scroll(
                    scroll_id=scroll_id, scroll=scroll_time
                )

            hits = elastic_response.get("hits", {}).get("hits", [])
            result_list = []
            for hit in hits:
                source = hit["_source"]
                source["_id"] = hit["_id"]
                result_list.append(source)
            return result_list, scroll_id, None
        except Exception as e:
            logging.error(f"[ElasticSearchClient] {e}")
            return None, None, str(e)

    async def delete(self, index: str, file_id: str) -> bool:
        """
        Delete ElasticSearch file
        params: file_id: File ID to delete
        return: True if deleted else False
        """
        try:
            self.client.delete(index=index, id=file_id)
            return True
        except Exception as e:
            logging.error(f"[ElasticSearchClient] {e}")
            return False
