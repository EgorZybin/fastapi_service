from fastapi.testclient import TestClient
from src.fastapi_service.main import app
import pytest

client = TestClient(app)


def test_add_url_to_queue():
    response = client.post("/browse", json={"url": "example.com"})
    assert response.status_code == 200
    assert response.json() == {"message": "URL added to queue", "url": "example.com"}


def test_add_invalid_url():
    response = client.post("/browse", json={"url": ""})
    assert response.status_code == 422
