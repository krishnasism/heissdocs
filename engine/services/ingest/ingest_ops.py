from services.ingest.ingest_client import IngestClient


def ingest_into_llm(pdf_body: dict) -> bool:
    ingest_client = IngestClient()
    return ingest_client.ingest_document(pdf_body)