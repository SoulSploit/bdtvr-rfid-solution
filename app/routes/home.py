from flask import Blueprint, render_template, abort

bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        # Optionally log the error here if logging is set up
        abort(500)  # Return a 500 error if rendering fails
