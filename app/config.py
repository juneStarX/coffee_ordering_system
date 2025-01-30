# coffee_ordering_system/app/config.py
# Defines environment-specific configurations (Dev, Test, Prod)

#The app loads the correct configuration based on the environment (FLASK_ENV).
#Secure & scalable—production DB credentials come from environment variables.

import os

class Config:
    """Base configuration (shared settings)."""
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Development-specific settings."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"
    ENABLE_DELIVERY = False  # Delivery disabled in development

class TestingConfig(Config):
    """Testing-specific settings."""
    TESTING = True
    #SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:" # Use in-memory database for tests rather than a persistent one
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENABLE_DELIVERY = False  # Delivery disabled in testing

class ProductionConfig(Config):
    """Production-specific settings."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://user:password@prod.db")
    ENABLE_DELIVERY = True  # Delivery enabled in production
