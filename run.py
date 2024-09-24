import os
import sys
from app import create_app

# Create an instance of the Flask application
app = create_app()

if __name__ == "__main__":
    # Determine if we should run in debug mode
    debug_mode = os.environ.get('FLASK_DEBUG', '0') == '1'
    port = int(os.environ.get('FLASK_PORT', 5000))  # Allow configurable port
    
    # Log the application startup
    app.logger.info(f"Starting application in {'debug' if debug_mode else 'production'} mode on port {port}.")

    try:
        app.run(host='0.0.0.0', port=port, debug=debug_mode)
    except Exception as e:
        app.logger.error(
