# Ioana A Mititean
# Unit 23 Exercise - Blogly App

"""
Models for Blogly.
"""

from flask_sqlalchemy import SQLAlchemy

PLACEHOLDER_IMG = "https://cdn.pixabay.com/photo/2016/08/08/09/17/avatar-1577909_960_720.png"
db = SQLAlchemy()


def connect_db(app):
    """
    Connect Flask app to database.
    """

    db.app = app
    db.init_app(app)


class User(db.Model):
    """
    Class representing a user.

    One user can have many posts.
    """

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    image_url = db.Column(db.Text, server_default=PLACEHOLDER_IMG)

    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")

    def get_full_name(self):
        """
        Return the full name for this user.
        """

        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        """
        String representation of this user: <User id, first_name, last_name>
        """

        return f"<User {self.id} {self.first_name} {self.last_name}>"


class Post(db.Model):
    """
    Class representing a post made by a user.

    One post can have only one user.
    """

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def get_formatted_datetime(self):
        """
        Return a string representing a nicer-formatted 'created at' date and time for this post.
        """

        return self.created_at.strftime("%b %d %Y, @%H:%M")

    def __repr__(self):
        """
        String representation of this post: <Post id, created_at, user_id>
        """

        return f"<Post {self.id} {self.created_at} {self.user_id}>"


class Tag(db.Model):
    """
    Class representing a tag for a post.

    One tag can have many posts, and one post can have many tags.
    """

    __tablename__ = "tags"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    name = db.Column(db.String(30), unique=True, nullable=False)

    posts = db.relationship("Post",
                            secondary="posts_tags",
                            backref="tags")


class PostTag(db.Model):
    """
    Class representing the joining of a Post and a Tag.

    Contains foreign keys for Post IDs and Tag IDs.
    """

    __tablename__ = "posts_tags"

    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"), primary_key=True)
