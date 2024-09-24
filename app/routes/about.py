from flask import Blueprint, render_template, abort
import logging

bp = Blueprint('about', __name__)

@bp.route('/about')
def about():
    try:
        return render_template('about.html')
    except Exception as e:
        # Optionally log the error
        logging.getLogger(__name__).error(f"Error rendering about template: {e}")
        abort(500)  # Return a 500 error if rendering fails
