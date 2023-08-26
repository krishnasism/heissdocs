import json
from temp_storage_manager import get_temp_file_stream, delete_file
from services.pdf.parsing.parser import get_pdf_body
from tempfile import NamedTemporaryFile
from services.storage.storage_ops import upload_file_to_bucket
from services.database.db_ops import put_pdf_to_document_db
from services.elasticsearch.elasticsearch_client import insert_document_to_elasticsearch
from services.ingest.ingest_ops import ingest_into_llm
from enums.FileStages import FileStages
from api_helpers import update_document_progress
import os
import logging
from uuid import uuid4


def process_file(message):
    file_params = json.loads(message)
    chunk_file_stream = get_temp_file_stream(
        file_params["chunk_file_name"], file_params["temp_bucket_name"]
    )
    full_file_stream = get_temp_file_stream(
        file_params["document_unique_id"], file_params["temp_bucket_name"]
    )
    document_unique_id = file_params["document_unique_id"]

    document_progress = {
        "user_email": file_params["user_email"],
        "document_id": document_unique_id,
        "document_name": file_params["original_file_name"],
        "stage": FileStages.PROCESSING.value,
        "pages_parsed": 0,
        "total_pages": file_params["total_pages"],
    }

    update_document_progress(document_progress)

    chunk_temp_file = NamedTemporaryFile(delete=False)
    with open(chunk_temp_file.name, "wb") as f:
        f.write(chunk_file_stream)

    pdf_body, file_metadata = get_pdf_body(
        pdf_file=chunk_temp_file,
        original_file_name=(file_params["original_file_name"]),
        document_progress=document_progress,
        force_ocr=file_params.get("force_ocr"),
    )

    full_temp_file = NamedTemporaryFile(delete=False)
    with open(full_temp_file.name, "wb") as f:
        f.write(full_file_stream)

    if file_params.get("store_files_in_cloud"):
        blob_file_name = document_unique_id + ".pdf"
        bucket_name = file_params["bucket_name"]
        with open(full_temp_file.name, "rb") as f:
            if bucket_name:
                response = upload_file_to_bucket(f, blob_file_name, bucket_name)
                if response:
                    file_metadata["blob_file_name"] = blob_file_name
                    file_metadata["bucket_name"] = bucket_name
    file_metadata[
        "file_name"
    ] = f"{str(file_metadata.get('filename'))}_{str(uuid4().hex)}"

    failures = []
    status = True

    if file_params.get("store_in_document_db"):
        status = put_pdf_to_document_db(pdf_body, file_metadata)
        if not status:
            failures.append("nosql")

    if file_params.get("ingest_into_llm"):
        status = ingest_into_llm(pdf_body, file_metadata)
        if not status:
            failures.append("llm")

    if file_params.get("store_in_elastic"):
        status = insert_document_to_elasticsearch(
            document=pdf_body, file_metadata=file_metadata
        )
        if not status:
            failures.append("elastic")

    if len(failures) > 0:
        document_progress["stage"] = FileStages.ERROR.value
        update_document_progress(document_progress)
        logging.error(
            f"[Process] Error while processing file. Failures: {failures}",
        )

    chunk_temp_file.close()
    os.remove(chunk_temp_file.name)
    full_temp_file.close()
    os.remove(full_temp_file.name)
    try:
        delete_file(file_params["chunk_file_name"], file_params["temp_bucket_name"])
        delete_file(file_params["document_unique_id"], file_params["temp_bucket_name"])
    except:
        logging.warning("[Process] Temp file could not be deleted from S3")
    return len(failures) == 0
