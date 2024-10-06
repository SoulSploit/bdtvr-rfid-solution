import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-default-secret-key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL') or 'DEBUG'

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or 'postgresql://username:password@localhost:5432/dev_db'

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or 'postgresql://username:password@localhost:5432/test_db'

class ProductionConfig(Config):
    """Production configuration."""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'postgresql://username:password@localhost:5432/prod_db'

# Factory method to get the appropriate configuration
def get_config(env='development'):
    if env == 'production':
        return ProductionConfig
    elif env == 'testing':
        return TestingConfig
    else:
        return DevelopmentConfig
