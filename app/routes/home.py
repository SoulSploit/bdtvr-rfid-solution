from flask import Blueprint, render_template, abort, current_app

bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    """Render the home page."""
    try:
        return render_template('index.html')
    except Exception as e:
        # Log the error for debugging purposes
        current_app.logger.error(f"Error rendering index page: {e}")
        abort(500)  # Return a 500 error if rendering fails

@bp.route('/about')
def about():
    """Render the about page."""
    try:
        return render_template('about.html')
    except Exception as e:
        # Log the error for debugging purposes
        current_app.logger.error(f"Error rendering about page: {e}")
        abort(500)  # Return a 500 error if rendering fails

@bp.route('/contact')
def contact():
    """Render the contact page."""
    try:
        return render_template('contact.html')
    except Exception as e:
        # Log the error for debugging purposes
        current_app.logger.error(f"Error rendering contact page: {e}")
        abort(500)  # Return a 500 error if rendering fails
