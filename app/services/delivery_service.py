#Implement the delivery service
#Encapsulate delivery logic inside a service class
#Can be expanded to integrate real delivery APIs

class DeliveryService:
    """Handles business logic for processing deliveries."""

    def process_delivery(self, customer_name, address, coffee_type):
        """Processes a delivery order and generates an order ID."""
        order_id = hash(f"{customer_name}-{address}-{coffee_type}") % 10000
        return {
            "message": f"Delivery confirmed: {coffee_type} for {customer_name} at {address}.",
            "order_id": order_id
        }
