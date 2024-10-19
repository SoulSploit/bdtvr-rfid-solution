import os

class Config:
    """Base configuration with common settings."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')  # Default secret key
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable tracking modifications for performance
    LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'DEBUG')  # Default logging level

class DevelopmentConfig(Config):
    """Configuration settings for development."""
    DEBUG = True  # Enable debug mode
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI', 'postgresql://username:password@localhost:5432/dev_db')

class TestingConfig(Config):
    """Configuration settings for testing."""
    TESTING = True  # Enable testing mode
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI', 'postgresql://username:password@localhost:5432/test_db')

class ProductionConfig(Config):
    """Configuration settings for production."""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'postgresql://username:password@localhost:5432/prod_db')

def get_config(env=None):
    """Retrieve the appropriate configuration class based on the environment."""
    if env is None:
        env = os.environ.get('FLASK_ENV', 'development')  # Default to 'development' if not set
    
    if env == 'production':
        return ProductionConfig
    elif env == 'testing':
        return TestingConfig
    else:
        return DevelopmentConfig
