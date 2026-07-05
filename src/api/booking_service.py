import requests


class BookingService:
    def __init__(self, api_client):
        self.api_client = api_client
        self.endpoint = "/booking/"

    def create_booking(self, payload: dict) -> requests.Response:
        return self.api_client.post(self.endpoint, json=payload)
    
    def get_booking_by_id(self, booking_id: int) -> requests.Response:
        return self.api_client.get(f"{self.endpoint}{booking_id}")