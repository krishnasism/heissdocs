import boto3


def get_local_sqs_client():
    """Get local SQS client running in docker"""
    return boto3.client(
        "sqs",
        endpoint_url="http://sqs:9324",
        region_name="us-east-1",
        aws_access_key_id="x",
        aws_secret_access_key="x",
    )


def create_queue(client, queue_name="parsetask"):
    """Create queue for local sqs client"""
    client.create_queue(QueueName=queue_name)
    return get_queue_url(client, queue_name)


def get_queue_url(client, queue_name="parsetask"):
    """
    Get queue url for local sqs client
    """
    return client.get_queue_url(QueueName=queue_name)["QueueUrl"]
