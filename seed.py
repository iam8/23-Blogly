# Ioana A Mititean
# Unit 23 Exercise - Blogly App

"""
Seed file for Blogly app - add 3 initial users and some posts into database.
"""

from models import User, Post, Tag, PostTag, db
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

        # Create some tags and connect them to some posts
        tag1 = Tag(name="Tag1")
        tag2 = Tag(name="Tag2")
        tag3 = Tag(name="Tag3")

        db.session.add_all([tag1, tag2, tag3])
        db.session.commit()

        posttag1 = PostTag(post_id=post_jane.id, tag_id=tag1.id)
        posttag2 = PostTag(post_id=post_jane.id, tag_id=tag2.id)
        posttag3 = PostTag(post_id=post_jane2.id, tag_id=tag3.id)

        db.session.add_all([posttag1, posttag2, posttag3])
        db.session.commit()
