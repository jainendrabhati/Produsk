
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_book():
    response = client.post("/books", json={"title": "Test Book"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"
