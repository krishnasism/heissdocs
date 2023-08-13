import logging
from qdrant_client import qdrant_client


class QdrantClient:
    client = None

    def connect(self, host: str = None, port: int = None, api_key: str = None):
        """Connect to Qdrant"""
        if host:
            host = host.replace("http://", "")
            host = host.replace("https://", "")
        try:
            self.client = qdrant_client.QdrantClient(
                host=host,
                port=port,
                api_key=api_key,
            )
        except Exception as e:
            logging.error(f"[Qdrant Connection] {e}")
