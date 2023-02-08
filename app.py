# Ioana A Mititean
# Unit 23 Exercise - Blogly App

"""
Blogly application - Flask setup and routes.
"""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config["SECRET_KEY"] = "O secreta foarte secreta"
debug = DebugToolbarExtension(app)

with app.app_context():
    db.create_all()
