# Ensure authenticated users can place orders, while unauthenticated users are denied.

import json

def test_place_pickup_order(test_client, test_login):
    """Test placing a pickup order as an authenticated user."""
    headers = test_login  # ✅ Use the fixture

    response = test_client.post("/order", json={"customer_name": "badass", "coffee_type": "Latte"}, headers=headers)
    assert response.status_code == 200
    assert "Order confirmed" in response.json["message"]


def test_unauthorized_pickup_order(test_client):
    """Test placing a pickup order without authentication."""
    response = test_client.post("/order", json={"customer_name": "notAbadass", "coffee_type": "Latte"})
    response_data = response.get_json()

    assert response.status_code == 403
    assert response_data is not None, "Response body is empty"
    assert "Unauthorized" in response_data.get("error", "")
