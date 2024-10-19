from flask import current_app
from app import db
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    """User model for managing user data."""
    
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    posts = relationship('Post', back_populates='user')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        """Hash the password and store it."""
        self.password_hash = generate_password_hash(password)
        current_app.logger.info(f'Password set for user: {self.username}')

    def check_password(self, password):
        """Verify the provided password against the stored hash."""
        return check_password_hash(self.password_hash, password)

    @classmethod
    def create_user(cls, username, email, password):
        """Create a new user with a hashed password."""
        new_user = cls(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        current_app.logger.info(f'User created: {new_user}')
        return new_user

    @classmethod
    def get_user_by_id(cls, user_id):
        """Retrieve a user by their ID."""
        user = cls.query.get(user_id)
        if user:
            current_app.logger.info(f'User retrieved: {user}')
        else:
            current_app.logger.warning(f'User not found: {user_id}')
        return user

    @classmethod
    def get_user_by_username(cls, username):
        """Retrieve a user by their username."""
        user = cls.query.filter_by(username=username).first()
        if user:
            current_app.logger.info(f'User retrieved: {user}')
        else:
            current_app.logger.warning(f'User not found: {username}')
        return user

    def update_user(self, username=None, email=None):
        """Update the user's details."""
        if username:
            self.username = username
        if email:
            self.email = email
        db.session.commit()
        current_app.logger.info(f'User updated: {self}')

    def delete_user(self):
        """Delete the user from the database."""
        db.session.delete(self)
        db.session.commit()
        current_app.logger.info(f'User deleted: {self}')

# Sample usage (this would typically go in a separate script or route):
if __name__ == "__main__":
    # Example of creating a user
    new_user = User.create_user("john_doe", "john@example.com", "securepassword123")
    print(new_user)

    # Example of checking a password
    if new_user.check_password("securepassword123"):
        print("Password is correct!")
    else:
        print("Password is incorrect.")

    # Example of updating user details
    new_user.update_user(email="john.doe@example.com")
    print(new_user)

    # Example of deleting the user
    new_user.delete_user()
