from src.api.base_service import BaseService
import requests

class RoomService(BaseService):
    def __init__(self, api_client):
        super().__init__(api_client, endpoint="/room")
    
    def get_room_by_id(self, room_id: int) -> requests.Response:
        return self.api_client.get(f"{self.endpoint}/{room_id}")
    
    def update_room(self, room_id: int, payload: dict) -> requests.Response:
        return self.api_client.put(f"{self.endpoint}/{room_id}", json=payload)
    
    def delete_room(self, room_id: int) -> requests.Response:
        return self.api_client.delete(f"{self.endpoint}/{room_id}")
    
    def get_all_rooms(self) -> requests.Response:
        return self.api_client.get(self.endpoint)
    
    def create_room(self, payload: dict) -> requests.Response:
        return self.api_client.post(f"{self.endpoint}/", json=payload)
    