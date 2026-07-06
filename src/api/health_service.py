from src.api.base_service import BaseService
import requests

class HealthService(BaseService):
    def __init__(self, api_client):
        super().__init__(api_client, endpoint="/report/actuator/health")
    
    def check_health(self) -> requests.Response:
        return self.api_client.get(self.endpoint)