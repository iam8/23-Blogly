# Ioana A Mititean
# Unit 23 Exercise - Blogly App

"""
Models for Blogly.
"""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def connect_db(app):
    """
    Connect Flask app to database.
    """

    db.app = app
    db.init_app(app)
