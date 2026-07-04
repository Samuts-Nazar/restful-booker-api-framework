from src.config.settings import settings

def test_login_success(auth_service):
    username = settings.username
    password = settings.password

    response = auth_service.login(username, password)

    assert response.status_code == 200
    assert "token" in response.cookies

def test_login_invalid_credentials(auth_service):
    response = auth_service.login("admin", "wrong_password")
    
    assert response.status_code == 403