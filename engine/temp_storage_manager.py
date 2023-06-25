import boto3
import logging


def get_temp_storage_client():
    return boto3.client(
        "s3",
        endpoint_url="http://minio:9000",
        aws_access_key_id="minio",
        aws_secret_access_key="minio123",
    )


def get_temp_storage_resource():
    return boto3.resource(
        "s3",
        endpoint_url="http://minio:9000",
        aws_access_key_id="minio",
        aws_secret_access_key="minio123",
    )


def create_local_storage():
    s3 = get_temp_storage_client()
    bucket_name = "tempfiles"

    # create bucket if it doesn't already exist
    if bucket_name not in [bucket["Name"] for bucket in s3.list_buckets()["Buckets"]]:
        s3.create_bucket(Bucket=bucket_name)


def get_temp_file_stream(temp_file_name, temp_bucket_name):
    s3 = get_temp_storage_client()

    # read file contents from the bucket
    response = s3.get_object(Bucket=temp_bucket_name, Key=temp_file_name)
    file_contents = response["Body"].read()
    return file_contents


def delete_file(file_name, bucket_name):
    s3 = get_temp_storage_resource()
    try:
        obj = s3.Object(bucket_name, file_name)
        obj.delete()
    except Exception as e:
        logging.error(f"[AWS - TempFile Manager] Error: {str(e)}")
        return False
    return True
