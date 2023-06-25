from enum import Enum


class QueueMessageTypes(Enum):
    PARSING = "parsing"
    SETTINGS_UPDATED = "settings_updated"
