# Ioana A Mititean
# Unit 23 Exercise - Blogly App

"""
Blogly application.
"""

from flask import Flask, request, redirect, render_template
from models import db, connect_db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()
