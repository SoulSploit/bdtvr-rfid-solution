from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy instance
db = SQLAlchemy()

def init_app(app):
    """Initialize the SQLAlchemy instance with the given Flask app.

    Args:
        app (Flask): The Flask application instance to bind the database.
    """
    db.init_app(app)
    # Optionally, you can create the database tables here
    # with app.app_context():
    #     db.create_all()
