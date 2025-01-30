#This fixture sets a new database for each test run

import pytest
from app import create_app
from app.models import db

@pytest.fixture
def test_client():
    """Creates a Flask test client with the testing configuration."""
    app = create_app("testing")  # ✅ Use TestingConfig
    app.config["TESTING"] = True

    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # ✅ Set up test database
        yield client  # ✅ Provide the client for testing
        with app.app_context():
            db.drop_all()  # ✅ Clean up after tests

@pytest.fixture
def test_login(test_client):
    """Creates a test user and logs in to get a valid token."""
    test_client.post("/auth/signup", json={"username": "badass", "password": "password123"})
    response = test_client.post("/auth/login", json={"username": "badass", "password": "password123"})
    token = response.json.get("token")
    assert token is not None, "Login failed: No token received"
    return {"Authorization": token}  # ✅ Return correct headers 
