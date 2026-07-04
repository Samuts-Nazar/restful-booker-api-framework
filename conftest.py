import pytest
from src.config.settings import settings
from src.api.client import ApiClient
from src.api.auth_service import AuthService

@pytest.fixture(scope="session")
def auth_client():
    return ApiClient(
        base_url=settings.auth_url, 
        timeout=settings.default_timeout
    )

@pytest.fixture
def auth_service(auth_client):
    return AuthService(auth_client)