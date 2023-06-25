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

    @classmethod
    def get_api_token(cls):
        if cls._instance is None:
            cls._instance = APIToken()
        return cls._instance
