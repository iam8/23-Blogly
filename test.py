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

        with app.test_client() as client:
            resp = client.get("/")

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "/users")

    def test_homepage_redirect_followed(self):
        """
        Test that GET '/' redirects to a page with the appropriate content.
        """

        with app.test_client() as client:
            resp = client.get("/", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Users</h1>", html)
            self.assertIn("<button>Add user</button>", html)
