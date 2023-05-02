import boto3
import logging

def get_temp_storage_client():
    return boto3.resource('s3', endpoint_url='http://minio:9000',
                        aws_access_key_id='minio', aws_secret_access_key='minio123')


def upload_file_to_blob(filestream, filename, bucket='tempfiles'):
    s3_client = get_temp_storage_client()
    try:
        if ".pdf" in filename:
            pdf_object = s3_client.Object(bucket, filename)
            response = pdf_object.put(
                Body=filestream, ContentType='application/pdf')
        else:
            pdf_object = s3_client.Object(bucket, filename)
            response = pdf_object.put(Body=filestream)
    except Exception as e:
        logging.error(f"[AWS - TempFile Manager] Error: {str(e)}")
        return False
    return True
