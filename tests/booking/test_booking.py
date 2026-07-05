
from urllib import response


def test_create_booking_success(booking_service, booking_payload):
    response = booking_service.create_booking(booking_payload)

    assert response.status_code == 201

    data = response.json()
    assert "bookingid" in data

    booking = data["booking"]
    assert booking["roomid"] == booking_payload["roomid"]
    assert booking["firstname"] == booking_payload["firstname"]
    assert booking["lastname"] == booking_payload["lastname"]
    assert booking["depositpaid"] == booking_payload["depositpaid"]
    assert booking["bookingdates"] == booking_payload["bookingdates"]

def test_get_booking_by_id_e2e(booking_service, booking_payload, auth_service):

    from src.config.settings import settings
    auth_response = auth_service.login(settings.username, settings.password)
    assert auth_response.status_code == 200

    # ДЕБАГ: дивимось куки і тіло відповіді авторизації
    print(f"\n[DEBUG] Auth Cookies: {auth_response.cookies.get_dict()}")
    print(f"[DEBUG] Auth Body: {auth_response.text}")

    token_cookie = auth_response.cookies.get("token")
    booking_service.api_client.session.headers.update({"Cookie": f"token={token_cookie}"})

    create_response = booking_service.create_booking(booking_payload)
    assert create_response.status_code == 201
    booking_id = create_response.json()["bookingid"]

    get_response = booking_service.get_booking_by_id(booking_id)
    assert get_response.status_code == 200

    retrieved_booking = get_response.json()
    assert retrieved_booking["roomid"] == booking_payload["roomid"]
    assert retrieved_booking["firstname"] == booking_payload["firstname"]
    assert retrieved_booking["lastname"] == booking_payload["lastname"]
    assert retrieved_booking["depositpaid"] == booking_payload["depositpaid"]
    assert retrieved_booking["bookingdates"] == booking_payload["bookingdates"]