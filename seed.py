# Ioana A Mititean
# Unit 23 Exercise - Blogly App

"""
Seed file for Blogly app - add 3 initial users into database.
"""

from models import User, db
from app import app

# Drop and create all tables
with app.app_context():
    db.drop_all()
    db.create_all()

    User.query.delete()

    # Add users
    jane = User(first_name="Jane", last_name="Doe")
    xavier = User(first_name="Xavier", last_name="Xavies", image_url="dummylink")
    ally = User(first_name="Ally", last_name="Andrews", image_url="dummylink2")

    # Add users to session and commit
    db.session.add_all([jane, xavier, ally])
    db.session.commit()
