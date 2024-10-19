from flask import current_app
from app import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Post(db.Model):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='posts')

    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return f'<Post {self.title}>'

    @classmethod
    def create_post(cls, title, content, user_id):
        """Create a new post."""
        new_post = cls(title=title, content=content, user_id=user_id)
        db.session.add(new_post)
        db.session.commit()
        current_app.logger.info(f'Post created: {new_post}')
        return new_post

    @classmethod
    def get_all_posts(cls):
        """Retrieve all posts."""
        posts = cls.query.all()
        current_app.logger.info(f'Retrieved {len(posts)} posts.')
        return posts

    @classmethod
    def get_post_by_id(cls, post_id):
        """Retrieve a post by its ID."""
        post = cls.query.get(post_id)
        if post:
            current_app.logger.info(f'Post retrieved: {post}')
        else:
            current_app.logger.warning(f'Post not found: {post_id}')
        return post

    def update_post(self, title=None, content=None):
        """Update the post's title and/or content."""
        if title:
            self.title = title
        if content:
            self.content = content
        db.session.commit()
        current_app.logger.info(f'Post updated: {self}')

    def delete_post(self):
        """Delete the post."""
        db.session.delete(self)
        db.session.commit()
        current_app.logger.info(f'Post deleted: {self}')
