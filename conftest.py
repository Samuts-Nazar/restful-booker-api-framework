from faker import Faker
import pytest
from src.config.settings import settings
from src.api.client import ApiClient
from src.api.auth_service import AuthService
from src.api.booking_service import BookingService

fake = Faker()

@pytest.fixture
def booking_payload():
    checkin = fake.date_between(start_date='+1d', end_date='+10d')
    checkout = fake.date_between(start_date='+15d', end_date='+30d')

    return {
        "roomid": 1,
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "depositpaid": fake.boolean(),
        "email": fake.email(),
        "phone": fake.numerify("###########"), # 11 цифр
        "bookingdates": {
            "checkin": checkin.strftime("%Y-%m-%d"),
            "checkout": checkout.strftime("%Y-%m-%d")
        }
    }

@pytest.fixture(scope="session")
def auth_client():
    return ApiClient(
        base_url=settings.auth_url, 
        timeout=settings.default_timeout
    )

@pytest.fixture(scope="session")
def booking_client():
    return ApiClient(
        base_url=settings.booking_url, 
        timeout=settings.default_timeout
    )

@pytest.fixture
def booking_service(booking_client):
    return BookingService(booking_client)

@pytest.fixture
def auth_service(auth_client):
    return AuthService(auth_client)