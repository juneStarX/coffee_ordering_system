# Confirms that signup and login work correctly.

import json

def test_signup(test_client):
    """Test user signup functionality."""
    response = test_client.post("/auth/signup", json={"username": "badass", "password": "password123"})
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data["message"] == "User badass registered successfully"

def test_login(test_client):
    """Test user login and token generation."""
    test_client.post("/auth/signup", json={"username": "badass", "password": "password123"})
    response = test_client.post("/auth/login", json={"username": "badass", "password": "password123"})
    #data = json.loads(response.data)
    token = response.json.get("token")

    assert token is not None, "Login failed: No token received"
    
    #assert response.status_code == 200
    #assert "token" in data  # ✅ Token should be returned
    #return data["token"]
