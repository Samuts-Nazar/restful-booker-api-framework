class BaseService:
    def __init__(self, api_client, endpoint: str):
        self.api_client = api_client
        self.endpoint = endpoint

    def login(self, username, password):
        payload = {
            "username": username,
            "password": password
        }
        response = self.api_client.post(self.endpoint, json=payload)
        return response