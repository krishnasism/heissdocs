from enum import Enum


class QueueMessageTypes(Enum):
    PARSING = 'parsing'
    S3_PARSING = 's3_parsing'
    SETTINGS_UPDATED = 'settings_updated'
