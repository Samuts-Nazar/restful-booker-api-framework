from faker import Faker
import pytest

from src.config.settings import settings
from src.api.client import ApiClient
from src.api.auth_service import AuthService
from src.api.booking_service import BookingService
from src.api.room_service import RoomService
from src.api.health_service import HealthService
from src.database.connection import DatabaseConnection

fake = Faker()

@pytest.fixture
def auth_token(auth_service):
    auth_response = auth_service.login(settings.username, settings.password)
    return auth_response.cookies.get("token")


# --- Clients (session-scope) ---

@pytest.fixture(scope="session")
def auth_client():
    return ApiClient(base_url=settings.auth_url, timeout=settings.default_timeout)


@pytest.fixture(scope="session")
def booking_client():
    return ApiClient(base_url=settings.booking_url, timeout=settings.default_timeout)


@pytest.fixture(scope="session")
def room_client():
    return ApiClient(base_url=settings.room_url, timeout=settings.default_timeout)


@pytest.fixture(scope="session")
def health_client():
    return ApiClient(base_url=settings.health_url, timeout=settings.default_timeout)


# --- Services (function-scope) ---

@pytest.fixture
def auth_service(auth_client):
    return AuthService(auth_client)


@pytest.fixture
def booking_service(booking_client):
    return BookingService(booking_client)


@pytest.fixture
def room_service(room_client):
    return RoomService(room_client)


@pytest.fixture
def health_service(health_client):
    return HealthService(health_client)


# --- Payloads ---

@pytest.fixture
def booking_payload():
    checkin = fake.date_between(start_date='+1d', end_date='+10d')
    checkout = fake.date_between(start_date='+15d', end_date='+30d')
    return {
        "roomid": fake.unique.random_int(min=1, max=1000000),
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "depositpaid": fake.boolean(),
        "email": fake.email(),
        "phone": fake.numerify("###########"),
        "bookingdates": {
            "checkin": checkin.strftime("%Y-%m-%d"),
            "checkout": checkout.strftime("%Y-%m-%d")
        }
    }


@pytest.fixture
def room_payload():
    return {
        "roomName": str(fake.unique.random_int(min=100, max=999)),
        "type": fake.random_element(["Single", "Double", "Suite"]),
        "accessible": fake.boolean(),
        "image": f"/images/room{fake.random_int(min=1, max=10)}.jpg",
        "description": fake.sentence(),
        "features": fake.random_elements(["TV", "WiFi", "Safe", "Radio", "Mini Bar"], length=3, unique=True),
        "roomPrice": fake.random_int(min=50, max=500)
    }


# --- Database ---

@pytest.fixture
def db_cursor():
    db = DatabaseConnection(
        jdbc_url=settings.db_jdbc_url,
        driver_class=settings.db_driver_class,
        jar_path=settings.db_jar_path,
        username=settings.db_username,
        password=settings.db_password
    )
    connection = db.connect()
    cursor = db.cursor()
    yield cursor
    connection.close()