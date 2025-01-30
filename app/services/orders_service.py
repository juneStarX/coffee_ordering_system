#Implement orders service
#Encapsulate order logic inside a service class

class OrderService:
    """Handles order processing logic."""

    def process_order(self, customer_name, coffee_type):
        order_id = hash(f"{customer_name}-{coffee_type}") % 10000
        return {"message": f"Order confirmed: {coffee_type} for {customer_name}.", "order_id": order_id}
