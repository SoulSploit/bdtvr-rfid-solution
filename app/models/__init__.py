from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy instance
db = SQLAlchemy()

def init_app(app):
    """Initialize the models with the Flask app."""
    db.init_app(app)