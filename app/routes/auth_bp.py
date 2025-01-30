#Implement authentication
#Authentication logic is handled by AuthService

from flask import Blueprint, request, jsonify
from app.services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    response = AuthService().create_user(data["username"], data["password"])
    return jsonify(response)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    response = AuthService().authenticate(data["username"], data["password"])
    return jsonify(response)
