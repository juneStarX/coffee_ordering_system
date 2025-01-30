#Implement the Factory Pattern
#Application Factory: 'create_app()'
#Creates Flask app instances dynamically
#Enables/Disables delivery dynamically

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import DevelopmentConfig, TestingConfig, ProductionConfig
from app.models import db
from app.routes.home_bp import home_bp
from app.routes.orders_bp import orders_bp
from app.routes.delivery_bp import delivery_bp
from app.routes.auth_bp import auth_bp

def create_app(config_name="development"):
    """Factory function that creates and configures a Flask app dynamically."""
    
    app = Flask(__name__)

    # Apply configurations
    if config_name == "development":
        app.config.from_object(DevelopmentConfig)
    elif config_name == "production":
        app.config.from_object(ProductionConfig)
    elif config_name == "testing":
        app.config.from_object(TestingConfig)

    # Initialize databse, ensures models are linked to Flask
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(orders_bp)
    
    # Conditionally register delivery routes
    if app.config.get("ENABLE_DELIVERY", False):
        app.register_blueprint(delivery_bp, url_prefix="/delivery")

    return app
