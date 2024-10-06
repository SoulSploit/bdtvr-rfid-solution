from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import logging
from config import get_config

# Initialize the database
db = SQLAlchemy()

def create_app(config_name='development'):
    """Create a Flask application instance."""
    app = Flask(__name__)

    # Load the configuration
    app.config.from_object(get_config(config_name))

    # Set up logging
    setup_logging(app)

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    register_blueprints(app)

    # Create the database tables
    with app.app_context():
        db.create_all()

    # Register error handlers
    register_error_handlers(app)

    return app

def setup_logging(app):
    """Configure logging for the application."""
    log_level = logging.DEBUG if app.debug else logging.INFO
    logging.basicConfig(level=log_level,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    app.logger.info("Logging is set up.")

def register_blueprints(app):
    """Register application blueprints."""
    from .routes import home, about  # Adjust this import as necessary
    app.register_blueprint(home.bp)
    app.register_blueprint(about.bp)
    app.logger.info("Blueprints registered.")

def log_error(app, error, level='error'):
    """Centralized error logging function."""
    log_method = app.logger.critical if level == 'critical' else app.logger.error
    log_method(f"Error: {error} - Request Path: {request.path} - Method: {request.method}")

def register_error_handlers(app):
    """Register error handlers for the application."""
    
    @app.errorhandler(404)
    def not_found(error):
        response = {"error": "Not found"}
        if app.config['DEBUG']:
            response['message'] = str(error)
        return jsonify(response), 404

    @app.errorhandler(500)
    def internal_error(error):
        log_error(app, error, level='critical')
        response = {"error": "Internal server error"}
        if app.config['DEBUG']:
            response['message'] = str(error)
        return jsonify(response), 500
