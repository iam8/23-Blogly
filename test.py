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
    Flask integration tests - tests for view functions.
    """

    def test_homepage_redirect(self):
        """
        Test that GET '/' results in a status code of 302 and redirects to the appropriate
        location.
        """

    def test_homepage_redirect_followed(self):
        """
        Test that GET '/' redirects to a page with the appropriate content.
        """


