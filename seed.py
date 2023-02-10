# Ioana A Mititean
# Unit 23 Exercise - Blogly App

"""
Seed file for Blogly app - add 3 initial users and some posts into database.
"""

from models import User, Post, db
from app import app, connect_db

if __name__ == "__main__":

    connect_db(app)

    # Drop and create all tables
    with app.app_context():
        db.drop_all()
        db.create_all()

        Post.query.delete()
        User.query.delete()

        # Create users
        jane = User(first_name="Jane", last_name="Doe")
        xavier = User(first_name="Xavier", last_name="Xavies", image_url="dummylink")
        ally = User(first_name="Ally", last_name="Andrews", image_url="dummylink2")

        db.session.add_all([jane, xavier, ally])
        db.session.commit()

        # Create some posts
        post_jane = Post(title="Jane's post",
                         content="This is a post by Jane",
                         user_id=jane.id)

        post_jane2 = Post(title="Jane's post 2",
                          content="This is another post by Jane",
                          user_id=jane.id)

        db.session.add_all([post_jane, post_jane2])
        db.session.commit()
