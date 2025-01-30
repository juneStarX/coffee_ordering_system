#Implement authentication decorator
#Only authenticated users can place orders

from functools import wraps
from flask import request, jsonify
from app.services.auth_service import AuthService

def require_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token or not AuthService().verify_token(token):
            return jsonify({"error": "Unauthorized"}), 403
        return f(*args, **kwargs)
    return decorated_function
