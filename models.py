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
    """

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    image_url = db.Column(db.Text, server_default=PLACEHOLDER_IMG)

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
