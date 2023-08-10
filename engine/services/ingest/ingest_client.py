import logging
from services.settings.settings import Settings
from services.qdrant.qdrant import QdrantClient
from services.ingest.utils import get_chunks
from langchain.vectorstores import Qdrant
from langchain.embeddings.openai import OpenAIEmbeddings

class IngestClient():
    client = None
    vector_store = None
    _settings = Settings.get_settings()

    def __init__(self):
        self.qdrant_client = QdrantClient()
        self.qdrant_client.get_collection()
        self.__create_vector_store()
    
    def __create_vector_store(self):
        collection_name = self._settings.qdrant_collection_name
        embeddings = OpenAIEmbeddings(
            openai_api_key=self._settings.openai_api_key,
        )
        self.vector_store = Qdrant(
            client=self.qdrant_client.client,
            collection_name=collection_name,
            embeddings=embeddings,
        )
    
    def ingest_document(self, pdf_body: dict) -> bool:
        """Ingest document"""
        full_text = ""
        try:
            for _, page_data in pdf_body.items():
                full_text += page_data
            text_chunks = get_chunks(full_text)
            self.vector_store.add_texts(text_chunks)
            return True
        except Exception as e:
            logging.exception(f"[LLM Ingest] {e}")
            return False
