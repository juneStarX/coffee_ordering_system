#Implement authentication service

import hashlib, secrets

class AuthService:
    """Handles authentication logic."""

    users_db = {}
    tokens_db = {}

    def create_user(self, username, password):
        if username in self.users_db:
            return {"error": "Username already exists"}
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.users_db[username] = hashed_password
        return {"message": f"User {username} registered successfully"}

    def authenticate(self, username, password):
        if username not in self.users_db:
            return {"error": "User not found"}
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if self.users_db[username] != hashed_password:
            return {"error": "Invalid password"}
        token = secrets.token_hex(16)
        self.tokens_db[token] = username
        return {"message": f"User {username} logged in successfully", "token": token}

    def verify_token(self, token):
        return self.tokens_db.get(token)
