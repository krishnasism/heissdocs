import logging
from qdrant_client import qdrant_client
from langchain.vectorstores import Qdrant
from langchain.embeddings.openai import OpenAIEmbeddings


class QdrantClient:
    client = None

    def connect(self, host: str = None, port: int = None, api_key: str = None):
        """Connect to Qdrant"""
        try:
            self.client = qdrant_client.QdrantClient(
                host=host,
                port=port,
                api_key=api_key,
            )
        except Exception as e:
            logging.error(f"[Qdrant Connection] {e}")

    def get_collection(self, collection_name: str = None):
        """Get collection"""
        try:
            collection = self.client.get_collection(collection_name)
            return collection
        except Exception as e:
            logging.error(f"[Qdrant Connection] {e}")

    def create_collection(self, collection_name: str):
        """Create collection"""
        # TODO: Add condition based on embedding
        vectors_config = qdrant_client.http.models.VectorParams(
            size=1536,
            distance=qdrant_client.http.models.Distance.COSINE,
        )
        try:
            collection = self.client.recreate_collection(
                collection_name,
                vectors_config=vectors_config,
            )
            return collection
        except Exception as e:
            logging.error(f"[Qdrant Connection] {e}")
