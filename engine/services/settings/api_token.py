from datetime import datetime
import base64
import json


class APIToken:
    _instance = None
    api_token = ""

    def __init__(self):
        if APIToken._instance is not None:
            raise Exception("APIToken class is a singleton!")
        else:
            APIToken._instance = self

    def update_api_token(self, api_token: str):
        self.api_token = api_token

    def is_token_expired(self) -> bool:
        if not self.api_token:
            return True
        token_parts = self.api_token.split(".")
        if len(token_parts) != 3:
            return True
        payload = token_parts[1] + "=="
        payload_bytes = payload.encode("utf-8")
        payload_decoded = payload_bytes.decode("utf-8")
        payload_json: dict = json.loads(base64.b64decode(payload_decoded))

        expiration_time = payload_json.get("exp")
        if not expiration_time:
            return True
        expiration_time = datetime.fromtimestamp(expiration_time)
        current_time = datetime.utcnow()
        return current_time > expiration_time

    @classmethod
    def get_api_token(cls):
        if cls._instance is None:
            cls._instance = APIToken()
        return cls._instance
