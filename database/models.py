from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    """User model for storing user details."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    # Relationship to Snippets
    snippets = db.relationship('Snippet', backref='user', lazy=True)

class Snippet(db.Model):
    """Snippet model for storing code snippets."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    code = db.Column(db.Text, nullable=False)
    tags = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"<Snippet {self.title}>"
