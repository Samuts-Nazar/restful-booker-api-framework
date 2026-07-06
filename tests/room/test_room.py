import pytest
from src.config.settings import settings
from src.models.room import RoomResponse


def test_create_room_success(room_service, room_payload, auth_token):
    room_service.api_client.session.headers.update({"Cookie": f"token={auth_token}"})
    response = room_service.create_room(room_payload)
    assert response.status_code == 201
    data = response.json()
    assert "roomid" in data
    assert data["roomName"] == room_payload["roomName"]
    assert data["type"] == room_payload["type"]
    assert data["accessible"] == room_payload["accessible"]
    assert data["image"] == room_payload["image"]
    assert data["roomPrice"] == room_payload["roomPrice"]


def test_get_room_by_id(room_service, room_payload, auth_token):
    room_service.api_client.session.headers.update({"Cookie": f"token={auth_token}"})
    create_response = room_service.create_room(room_payload)
    assert create_response.status_code == 201
    room_id = create_response.json()["roomid"]

    get_response = room_service.get_room_by_id(room_id)
    assert get_response.status_code == 200
    retrieved_room = RoomResponse(**get_response.json())
    assert retrieved_room.roomid == room_id
    assert retrieved_room.roomName == room_payload["roomName"]
    assert retrieved_room.type == room_payload["type"]
    assert retrieved_room.accessible == room_payload["accessible"]
    assert retrieved_room.image == room_payload["image"]
    assert retrieved_room.roomPrice == room_payload["roomPrice"]


def test_get_all_rooms(room_service, room_payload, auth_token):
    room_service.api_client.session.headers.update({"Cookie": f"token={auth_token}"})
    create_response = room_service.create_room(room_payload)
    assert create_response.status_code == 201

    get_all_response = room_service.get_all_rooms()
    assert get_all_response.status_code == 200
    rooms = get_all_response.json()["rooms"]
    assert any(room["roomid"] == create_response.json()["roomid"] for room in rooms)


def test_get_room_by_id_not_found(room_service, auth_token):
    room_service.api_client.session.headers.update({"Cookie": f"token={auth_token}"})
    response = room_service.get_room_by_id(-1)
    assert response.status_code == 404


@pytest.mark.parametrize("missing_field", ["roomName", "type", "roomPrice"])
def test_create_room_missing_required_fields(room_service, room_payload, auth_token, missing_field):
    room_service.api_client.session.headers.update({"Cookie": f"token={auth_token}"})
    invalid_payload = room_payload.copy()
    del invalid_payload[missing_field]

    response = room_service.create_room(invalid_payload)
    assert response.status_code == 400