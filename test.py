# Ioana A Mititean
# Unit 23 Exercise - Blogly App

"""
Tests for Blogly application.
"""

from unittest import TestCase
from app import app

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class FlaskTests(TestCase):
    """
    Flask integration tests - view functions.
    """


