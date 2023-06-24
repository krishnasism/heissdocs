from enum import Enum


class QueueMessageTypes(Enum):
    PARSING = 'parsing'
    PARSING_S3 = 'parsing_s3'
    SETTINGS_UPDATED = 'settings_updated'
