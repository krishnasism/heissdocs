from queue_manager import get_local_sqs_client, get_queue_url, create_queue
from temp_storage_manager import create_local_storage
import logging
from api_callers import get_auth_token, process_file

MAX_RETRIES = 20
sqs = get_local_sqs_client()
try:
    queue_url = get_queue_url(sqs, 'parse_task')
except:
    queue_url = create_queue(sqs, 'parse_task')

create_local_storage()
api_token = get_auth_token()

logging.info("[Queue Handler] Token acquired..")

while True:
    # Receive messages from the queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=20
    )

    messages = response.get('Messages', [])
    for message in messages:
        process_file(message['Body'], api_token)
        receipt_handle = message['ReceiptHandle']
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )
