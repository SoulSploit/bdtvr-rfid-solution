from flask import Flask
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

    # Create the database tables (if necessary)
    with app.app_context():
        db.create_all()

    # Error handling
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
    from routes.home import bp as home_bp
    from routes.about import bp as about_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)

    app.logger.info("Blueprints registered.")

def register_error_handlers(app):
    """Register error handlers for the application."""

    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 errors."""
        response = {"error": "Not found"}
        if app.config['DEBUG']:
            response['message'] = str(error)
        return response, 404

    @app.errorhandler(500)
    def internal_error(error):
        """Handle 500 errors."""
        app.logger.error(f"Internal server error: {error}")
        response = {"error": "Internal server error"}
        if app.config['DEBUG']:
            response['message'] = str(error)
        return response, 500

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
