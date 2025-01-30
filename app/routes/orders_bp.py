#Implement orders blueprint
#Enforce login before placing an order using @require_login

from flask import Blueprint, request, jsonify
from app.services.orders_service import OrderService
from app.utils.auth import require_login

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/order', methods=['POST'])
@require_login
def place_order():
    data = request.json
    response = OrderService().process_order(data["customer_name"], data["coffee_type"])
    return jsonify(response)
