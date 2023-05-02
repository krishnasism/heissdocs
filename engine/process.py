
import json
from temp_storage_manager import get_temp_file_stream, delete_file
from services.pdf.parsing.parser import get_pdf_body
from tempfile import NamedTemporaryFile
from services.storage.storage_ops import upload_file_to_blob
from services.database.db_ops import put_pdf_to_database
from enums.FileStages import FileStages
from api_helpers import update_document_progress
import os
import logging


def process_file(message):
    file_params = json.loads(message)
    file_stream = get_temp_file_stream(
        file_params['temp_file_name'], file_params['temp_bucket_name'])
    document_unique_id = file_params['document_unique_id']

    document_progress = {
        'user_email': file_params['user_email'],
        'document_id': document_unique_id,
        'document_name': file_params['original_file_name'],
        'stage': FileStages.PROCESSING.value,
        'pages_parsed': 0,
        'total_pages': 0
    }

    update_document_progress(document_progress)

    temp_file = NamedTemporaryFile(delete=False)
    with open(temp_file.name, 'wb') as f:
        f.write(file_stream)

    pdf_body, file_metadata = get_pdf_body(pdf_file=temp_file,
                                           original_file_name=(
                                               file_params['original_file_name']),
                                           store_files_in_cloud=file_params['store_files_in_cloud'],
                                           bucket_name=file_params['bucket_name'],
                                           document_progress=document_progress
                                           )

    if file_params['store_files_in_cloud']:
        blob_file_name = document_unique_id + ".pdf"
        bucket_name = file_params['bucket_name']
        with open(temp_file.name, "rb") as f:
            if bucket_name:
                response = upload_file_to_blob(f, blob_file_name, bucket_name)
                if response:
                    file_metadata['s3_blob_file_name'] = blob_file_name
                    file_metadata['s3_bucket_name'] = bucket_name

    status = put_pdf_to_database(pdf_body, file_metadata)
    temp_file.close()
    os.remove(temp_file.name)
    try:
        delete_file(file_params['temp_file_name'],
                    file_params['temp_bucket_name'])
    except:
        logging.warning('[Process] File could not be deleted from S3')

    if status:
        return True
    else:
        return False
