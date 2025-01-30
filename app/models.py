# coffee_ordering_system/app/models.py
# Uses SQLAlchemy ORM to define User, Order, and DeliveryOrder models.
# Easily extendable—can add relationships (e.g., users linked to orders).

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()  # ✅ Create SQLAlchemy instance

class User(db.Model):
    """User model for authentication."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.username}>"

class Order(db.Model):
    """Order model for pickup orders."""
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(80), nullable=False)
    coffee_type = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Order {self.coffee_type} for {self.customer_name}>"

class DeliveryOrder(db.Model):
    """Delivery order model."""
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    coffee_type = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<DeliveryOrder {self.coffee_type} for {self.customer_name} at {self.address}>"
