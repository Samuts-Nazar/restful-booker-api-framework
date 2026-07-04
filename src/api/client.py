import requests
from requests import Response

class ApiClient:
    def __init__(self, base_url: str, timeout: int):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()

    def _request(self, method: str, endpoint: str, **kwargs) -> Response:
        kwargs.setdefault('timeout', self.timeout)
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        try:
            response = self.session.request(method, url, **kwargs)
            return response
        except requests.exceptions.RequestException as e:
            print(f"API Request failed: {method} {url} - {e}")
            raise


    def get(self, endpoint: str, **kwargs) -> Response:
        return self._request("GET", endpoint, **kwargs)
    
    def post(self, endpoint: str, data=None, json=None, **kwargs) -> Response:
        return self._request("POST", endpoint, data=data, json=json, **kwargs)

    def put(self, endpoint: str, data=None, json=None, **kwargs) -> Response:
        return self._request("PUT", endpoint, data=data, json=json, **kwargs)

    def patch(self, endpoint: str, data=None, json=None, **kwargs) -> Response:
        return self._request("PATCH", endpoint, data=data, json=json, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> Response:
        return self._request("DELETE", endpoint, **kwargs)