from queue_manager import get_local_sqs_client, get_queue_url, create_queue
from temp_storage_manager import create_local_storage
import logging
from api_helpers import get_auth_token, get_settings
from process import process_file
from enums.QueueMessages import QueueMessageTypes
from services.settings.settings import Settings
from services.settings.api_token import APIToken
from services.settings.env_loader import load_env_file
import json

load_env_file()
MAX_RETRIES = 20
sqs = get_local_sqs_client()
try:
    queue_url = get_queue_url(sqs, "parse_task")
except:
    queue_url = create_queue(sqs, "parse_task")

create_local_storage()
api_token = get_auth_token()
api_token_obj = APIToken.get_api_token()
api_token_obj.update_api_token(api_token)

logging.info("[Queue Handler] Token acquired..")

settings_obj = Settings.get_settings()

while True:
    # Receive messages from the queue
    response = sqs.receive_message(
        QueueUrl=queue_url, MaxNumberOfMessages=1, WaitTimeSeconds=20
    )

    messages = response.get("Messages", [])
    for message in messages:
        logging.info("Processing file...")
        try:
            message_body = json.loads(message["Body"])
            if message_body.get("message_type") == QueueMessageTypes.PARSING.value:
                process_file(message["Body"])
            elif (
                message_body.get("message_type")
                == QueueMessageTypes.SETTINGS_UPDATED.value
            ):
                settings = get_settings(message_body["user_email"])["settings"]
                settings_obj.update_settings(settings)

            receipt_handle = message["ReceiptHandle"]
        except Exception as e:
            logging.exception("Unable to Parse File", e)
        finally:
            sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
