def test_health_check(health_service):
    response = health_service.check_health()
    assert response.status_code == 200
    assert response.json() == {"status": "UP"}