from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_time_without_timezone():
    response = client.get("/time")
    assert response.status_code == 200
    assert "currentTime" in response.json()
    assert "adjustedTime" in response.json()


def test_get_time_with_valid_timezone():
    response = client.get("/time?timezone=+05:30")
    assert response.status_code == 200
    assert "currentTime" in response.json()
    assert "adjustedTime" in response.json()


def test_get_time_with_invalid_timezone():
    response = client.get("/time?timezone=invalid")
    assert response.status_code == 400
