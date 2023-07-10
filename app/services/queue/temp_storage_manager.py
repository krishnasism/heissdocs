import boto3
import logging


def get_temp_storage_client():
    """Get local S3 client running in docker"""
    return boto3.resource(
        "s3",
        endpoint_url="http://minio:9000",
        aws_access_key_id="minio",
        aws_secret_access_key="minio123",
    )


def upload_file_to_s3_bucket(filestream, filename: str, bucket="tempfiles"):
    """
    Upload file to S3 bucket
    params: filestream: File stream (BufferedReader)
    params: filename: File name
    params: bucket: Bucket name
    return: bool: True if file uploaded successfully, False otherwise
    """
    s3_client = get_temp_storage_client()
    try:
        if ".pdf" in filename:
            pdf_object = s3_client.Object(bucket, filename)
            _ = pdf_object.put(Body=filestream, ContentType="application/pdf")
        else:
            pdf_object = s3_client.Object(bucket, filename)
            _ = pdf_object.put(Body=filestream)
    except Exception as e:
        logging.error(f"[AWS - TempFile Manager] Error: {str(e)}")
        return False
    return True
