from fastapi.testclient import TestClient
from main import app
from bson import ObjectId

client = TestClient(app)

def test_crud():
    # Create
    response = client.post("/create", json={
        "title": "Test Title",
        "short_desc": "Test Short Description",
        "description": "Test Description",
        "tags": ["tag1", "tag2"]
    })
    assert response.status_code == 200
    data = response.json()
    assert "title" in data
    assert data["title"] == "Test Title"
    item_id = str(data["_id"])

    # Read All
    response = client.get("/read")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(item["_id"] == item_id for item in data)

    # Update
    response = client.put(f"/update/{item_id}", json={
        "title": "Updated Title",
        "short_desc": "Updated Short Description",
        "description": "Updated Description",
        "tags": ["tag3", "tag4"]
    })
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == f"{item_id} updated."

    # Delete
    response = client.delete(f"/delete/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == f"{item_id} deleted."

    # Verify Deletion
    response = client.get("/read")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert all(item["_id"] != item_id for item in data)
