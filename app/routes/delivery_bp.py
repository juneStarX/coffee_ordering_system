#Implement delivery blueprint
#Delivery orders require authentication

from flask import Blueprint, request, jsonify
from app.services.delivery_service import DeliveryService
from app.utils.auth import require_login  # Import authentication decorator

delivery_bp = Blueprint('delivery', __name__)

@delivery_bp.route('/order', methods=['POST'])
@require_login  # Require login before placing a delivery order
def place_delivery_order():
    """Handle delivery orders."""
    data = request.json
    customer_name = data.get("customer_name")
    address = data.get("address")
    coffee_type = data.get("coffee_type")

    if not customer_name or not address or not coffee_type:
        return jsonify({"error": "Missing required fields"}), 400

    response = DeliveryService().process_delivery(customer_name, address, coffee_type)
    return jsonify(response)
