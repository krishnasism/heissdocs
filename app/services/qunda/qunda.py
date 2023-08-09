from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from services.qdrant.qdrant import QdrantClient
from settings.config import override_settings, get_settings
from settings.override_config import get_override_settings
from settings.config import Settings
from langchain.vectorstores import Qdrant
from langchain.embeddings.openai import OpenAIEmbeddings
from qdrant_client import QdrantClient as qdc
import logging

class Qunda:
    vector_store = None
    qa_client = None

    def __init__(self, settings: Settings, vector_db_client: qdc):
        collection_name = settings.qdrant_collection_name
        embeddings = OpenAIEmbeddings(
            openai_api_key=settings.openai_api_key,
        )

        self.vector_store = Qdrant(
            client=vector_db_client,
            collection_name=collection_name,
            embeddings=embeddings,
        )

        self.qa_client = RetrievalQA.from_chain_type(
            llm=OpenAI(openai_api_key=settings.openai_api_key),
            retriever=self.vector_store.as_retriever(),
        )

    def ask(self, question: str) -> str:
        response = self.qa_client.run(question)
        return response

def ask(user_email: str, question: str) -> str:
    qdrant_client = QdrantClient()
    settings = override_settings(get_settings(), get_override_settings(user_email))
    qdrant_client.connect(
        host=settings.qdrant_host,
        port=settings.qdrant_port,
        api_key=settings.qdrant_api_key,
    )
    qunda_client = Qunda(
        settings=settings,
        vector_db_client=qdrant_client.client,
    )
    try:
        answer = qunda_client.ask(
            question=question,
        )
        return answer
    except Exception as e:
        logging.error(f"[Qunda] {e}")
        return "Sorry, I couldn't find an answer to your question."
