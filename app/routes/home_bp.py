from flask import Blueprint, jsonify

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    """Default home route."""
    return jsonify({
        "message": "Welcome to the Coffee Ordering System!",
        "available_routes": {
            "/auth/signup": "Register a new user",
            "/auth/login": "Login and get an authentication token",
            "/order": "Place a pickup coffee order (requires authentication)",
            "/delivery/order": "Place a delivery coffee order (requires authentication)"
        }
    })

