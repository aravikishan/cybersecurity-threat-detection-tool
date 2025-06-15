import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/api/users/", json={"username": "testuser", "email": "test@example.com"})
    assert response.status_code == 200
    assert response.json()['username'] == 'testuser'

def test_get_alerts():
    response = client.get("/api/alerts/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)