import requests
from src.api.base_service import BaseService

class AuthService(BaseService):
    def __init__(self, api_client):
        super().__init__(api_client, endpoint="/auth/login")

    def login(self, username: str, password: str) -> requests.Response:
        payload = {
            "username": username,
            "password": password
        }
        response = self.api_client.post(self.endpoint, json=payload)
        return response