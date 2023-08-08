import logging
from services.settings.settings import Settings
from qdrant_client import QdrantClient as qdc
from langchain.vectorstores import Qdrant
from langchain.embeddings.openai import OpenAIEmbeddings


class QdrantClient:
    client = None
    _settings = Settings.get_settings()

    def __init__(self):
        self.__connect_to_qdrant()

    def __connect_to_qdrant(self):
        """Connect to Qdrant"""
        try:
            self.client = qdc(
                host=self._settings.qdrant_host,
                port=self._settings.qdrant_port,
                token=self._settings.qdrant_api_key,
            )
        except Exception as e:
            logging.error(f"[Qdrant Connection] {e}")

    def get_collection(self, collection_name: str = None):
        """Get collection"""
        if not collection_name:
            collection_name = self._settings.qdrant_collection_name
        try:
            collection = self.client.get_collection(collection_name)
            if collection is None:
                self.create_collection(self._settings.qdrant_collection_name)
                collection = self.client.get_collection(collection_name)
            return collection
        except Exception as e:
            logging.error(f"[Qdrant Connection] {e}")

    def create_collection(self, collection_name: str):
        """Create collection"""
        # TODO: Add condition based on embedding
        vectors_config = self.client.http.models.VectorParams(
            size=1536,
            distance=self.client.http.models.Distance.COSINE,
        )
        try:
            collection = self.client.recreate_collection(
                collection_name,
                vectors_config=vectors_config,
            )
            return collection
        except Exception as e:
            logging.error(f"[Qdrant Connection] {e}")
