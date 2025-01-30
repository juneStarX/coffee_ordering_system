# This test ensures that the home route is accessible (status_code = 200)
# The response contains a welcome message
# The response liosts API routes

import json

def test_home_route(test_client):
    """Test that the home route (`/`) returns a welcome message and available routes."""
    response = test_client.get("/")
    data = json.loads(response.data)

    assert response.status_code == 200
    assert "message" in data
    assert data["message"] == "Welcome to the Coffee Ordering System!"
    assert "available_routes" in data
    assert "/auth/signup" in data["available_routes"]
    assert "/auth/login" in data["available_routes"]
