import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-default-secret-key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable tracking modifications for performance
    LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'DEBUG')  # Set default logging level

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True  # Enable debug mode for development
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
        'postgresql://username:password@localhost:5432/dev_db'

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True  # Enable testing mode
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
        'postgresql://username:password@localhost:5432/test_db'

class ProductionConfig(Config):
    """Production configuration."""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'postgresql://username:password@localhost:5432/prod_db'

# Factory method to get the appropriate configuration
def get_config(env=None):
    """Return the configuration class based on the environment."""
    if env is None:
        env = os.environ.get('FLASK_ENV', 'development')  # Default to 'development' if not set
    
    if env == 'production':
        return ProductionConfig
    elif env == 'testing':
        return TestingConfig
    else:
        return DevelopmentConfig
