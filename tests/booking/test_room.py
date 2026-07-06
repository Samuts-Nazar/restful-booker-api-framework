from src.config.settings import settings

def test_create_room_success(room_service, room_payload, auth_service):
    auth_response = auth_service.login(settings.username, settings.password)
    token = auth_response.cookies.get("token")
    room_service.api_client.session.headers.update({"Cookie": f"token={token}"})

    response = room_service.create_room(room_payload)
    assert response.status_code == 201

    data = response.json()
    assert "roomid" in data
    assert data["roomName"] == room_payload["roomName"]
    assert data["type"] == room_payload["type"]
    assert data["accessible"] == room_payload["accessible"]
    assert data["image"] == room_payload["image"]
    assert data["roomPrice"] == room_payload["roomPrice"]

def test_get_room_by_id(room_service, room_payload, auth_service):
    auth_response = auth_service.login(settings.username, settings.password)
    token = auth_response.cookies.get("token")
    room_service.api_client.session.headers.update({"Cookie": f"token={token}"})

    create_response = room_service.create_room(room_payload)
    assert create_response.status_code == 201
    room_id = create_response.json()["roomid"]

    get_response = room_service.get_room_by_id(room_id)
    assert get_response.status_code == 200

    retrieved_room = get_response.json()
    assert retrieved_room["roomid"] == room_id
    assert retrieved_room["roomName"] == room_payload["roomName"]
    assert retrieved_room["type"] == room_payload["type"]
    assert retrieved_room["accessible"] == room_payload["accessible"]
    assert retrieved_room["image"] == room_payload["image"]
    assert retrieved_room["roomPrice"] == room_payload["roomPrice"]

def test_get_all_rooms(room_service, room_payload, auth_service):
    auth_response = auth_service.login(settings.username, settings.password)
    token = auth_response.cookies.get("token")
    room_service.api_client.session.headers.update({"Cookie": f"token={token}"})

    create_response = room_service.create_room(room_payload)
    assert create_response.status_code == 201

    get_all_response = room_service.get_all_rooms()
    assert get_all_response.status_code == 200

    rooms = get_all_response.json()["rooms"]
    assert any(room["roomid"] == create_response.json()["roomid"] for room in rooms)

def test_get_room_by_id_not_found(room_service, auth_service):
    auth_response = auth_service.login(settings.username, settings.password)
    token = auth_response.cookies.get("token")
    room_service.api_client.session.headers.update({"Cookie": f"token={token}"})

    response = room_service.get_room_by_id(-1)  # Assuming -1 is an invalid room ID
    assert response.status_code == 404