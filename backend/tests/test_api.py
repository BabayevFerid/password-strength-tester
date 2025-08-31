import json
from app import app

def test_password_strength():
    client = app.test_client()

    response = client.post("/api/check", json={"password": "weak"})
    data = json.loads(response.data)
    assert "strength" in data
    assert data["strength"] == "Weak"
