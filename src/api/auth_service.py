import requests

class AuthService:
    def __init__(self, api_client):
        self.api_client = api_client
        self.endpoint = "/auth/login"

    def login(self, username: str, password: str) -> requests.Response:
        payload = {
            "username": username,
            "password": password
        }
        response = self.api_client.post(self.endpoint, json=payload)
        return response