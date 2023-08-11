import logging
from services.settings.settings import Settings
from qdrant_client import qdrant_client
from qdrant_client.http import models


class QdrantClient:
    client = None
    _settings = Settings.get_settings()

    def __init__(self):
        self.__connect_to_qdrant()

    def __connect_to_qdrant(self):
        """Connect to Qdrant"""
        try:
            self.client = qdrant_client.QdrantClient(
                host=self._settings.qdrant_host,
                port=self._settings.qdrant_port,
                api_key=self._settings.qdrant_api_key,
            )
        except Exception as e:
            logging.error(f"[Qdrant Connection] {e}")

    def get_collection(self, collection_name: str = None):
        """Get collection"""
        collection = None
        if not collection_name:
            collection_name = self._settings.qdrant_collection_name
        try:
            collection = self.client.get_collection(collection_name)
            return collection
        except Exception as e:
            logging.error(f"[Qdrant Connection] {e}")
        try:
            if collection is None:
                self.create_collection(collection_name)
                collection = self.client.get_collection(collection_name)
                logging.info(
                    f"[Qdrant Connection] Created collection {collection_name}"
                )
            return collection
        except Exception as e:
            logging.error(f"[Qdrant Connection] {e}")

    def create_collection(self, collection_name: str):
        """Create collection"""
        # TODO: Add condition based on embedding
        vectors_config = models.VectorParams(
            size=1536,
            distance=models.Distance.COSINE,
        )
        try:
            collection = self.client.recreate_collection(
                collection_name,
                vectors_config=vectors_config,
            )
            return collection
        except Exception as e:
            logging.error(f"[Qdrant Connection] {e}")
