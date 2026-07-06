import requests
from src.api.base_service import BaseService

class BookingService(BaseService):
    def __init__(self, api_client):
        super().__init__(api_client, endpoint="/booking/")

    def create_booking(self, payload: dict) -> requests.Response:
        return self.api_client.post(self.endpoint, json=payload)
    
    def get_booking_by_id(self, booking_id: int) -> requests.Response:
        return self.api_client.get(f"{self.endpoint}{booking_id}")