from flask import Blueprint, render_template, abort, current_app

bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    """Render the home page."""
    return render_template_with_error_handling('index.html')

@bp.route('/about')
def about():
    """Render the about page."""
    return render_template_with_error_handling('about.html')

@bp.route('/contact')
def contact():
    """Render the contact page."""
    return render_template_with_error_handling('contact.html')

def render_template_with_error_handling(template_name):
    """Render a template with error handling.

    Args:
        template_name (str): The name of the template to render.

    Returns:
        Response: The rendered template or a 500 error if rendering fails.
    """
    try:
        return render_template(template_name)
    except Exception as e:
        # Log the error for debugging purposes
        current_app.logger.error(f"Error rendering {template_name}: {e}")
        abort(500)  # Return a 500 error if rendering fails
