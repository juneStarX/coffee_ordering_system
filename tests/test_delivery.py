# Ensures ENABLE_DELIVERY = False blocks /delivery/order in development/testing mode.

def test_delivery_route_not_available(test_client, test_login):
    """Test that delivery route is disabled in testing (development mode)."""
    #token = test_login(test_client)
    #headers = {"Authorization": token}

    headers = test_login

    response = test_client.post("/delivery/order", json={"customer_name": "badass", "address": "123 Coffee St.", "coffee_type": "Cappuccino"}, headers=headers)
    assert response.status_code == 404  # ✅ Delivery route should not be available
