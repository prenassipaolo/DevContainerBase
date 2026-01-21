from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_task():
    response = client.post(
        "/tasks/", json={"title": "Test Task", "description": "Writing tests"}
    )
    assert response.status_code == 201
    assert response.json()["title"] == "Test Task"


def test_read_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_invalid_task():
    response = client.get("/tasks/999")
    assert response.status_code == 404
