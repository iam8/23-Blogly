# Ioana A Mititean
# Unit 23 Exercise - Blogly App

"""
Tests for Blogly application.
"""

from unittest import TestCase
from app import app
from models import db, connect_db, User, Post

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///blogly_test_db"
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

connect_db(app)

with app.app_context():
    db.drop_all()
    db.create_all()


class FlaskTests(TestCase):
    """
    Flask integration tests - tests for view functions.
    """

    def setUp(self) -> None:
        """
        Add sample users and posts to test database.
        """

        with app.app_context():
            User.query.delete()
            Post.query.delete()

            user0 = User(first_name="first0", last_name="last0")

            db.session.add(user0)
            db.session.commit()

            self.user0_id = user0.id

            post0 = Post(title="Test post 0", content="Test 0 content", user_id=user0.id)
            post1 = Post(title="Test post 1", content="Test 1 content", user_id=user0.id)
            post2 = Post(title="Test post 2", content="Test 2 content", user_id=user0.id)

            db.session.add_all([post0, post1, post2])
            db.session.commit()

            self.post0_id = post0.id
            self.post1_id = post1.id
            self.post2_id = post2.id

        return super().setUp()

    def tearDown(self) -> None:
        """
        Clean up any fouled transaction.
        """

        with app.app_context():
            db.session.rollback()

        return super().tearDown()

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

# USER-RELATED TESTS ------------------------------------------------------------------------------

    def test_get_user_list(self):
        """
        Test that GET '/users' results in a status code of 200 and returns a page with the
        appropriate content.
        """

        with app.test_client() as client:
            resp = client.get("/users")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Users</h1>", html)
            self.assertIn("<button>Add user</button>", html)

    def test_get_new_user_form(self):
        """
        Test that GET '/users/new' results in a status code of 200 and returns a page with the
        appropriate content.
        """

        with app.test_client() as client:
            resp = client.get("/users/new")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Create A New User</h1>", html)
            self.assertIn("<button>Add</button>", html)
            self.assertRegex(html, '<form .* method="POST">')

    def test_get_user_details(self):
        """
        Test that GET '/users/<user_id> for an existing user results in a status code of 200 and
        returns a page with the appropriate content.
        """

        with app.test_client() as client:
            resp = client.get(f"/users/{self.user0_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>first0 last0</h1>", html)
            self.assertIn("<button>Edit</button>", html)
            self.assertIn("<button>Delete</button>", html)

    def test_get_user_edit_form(self):
        """
        Test that GET '/users/<user_id>/edit for an existing user results in a status code of 200
        and returns a page with the appropriate content.
        """

        with app.test_client() as client:
            resp = client.get(f"/users/{self.user0_id}/edit")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Edit User</h1>", html)
            self.assertIn("<button>Save</button>", html)
            self.assertIn("<button>Cancel</button>", html)
            self.assertRegex(html, '<form .* method="POST">')

    def test_add_new_user_redirect(self):
        """
        Test that adding a new user results in a status code of 302 and redirects to the correct
        location.
        """

        with app.test_client() as client:
            data = {"firstname": "Jane",
                    "lastname": "Doe",
                    "imageurl": "dummylink"}

            resp = client.post("/users/new",
                               data=data,
                               follow_redirects=False)

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "/users")

    def test_add_new_user_redirect_followed(self):
        """
        Test that adding a new user results in a status code of 200 and redirects to a page with
        the appropriate content.
        """

        with app.test_client() as client:
            data = {"firstname": "Jane",
                    "lastname": "Doe",
                    "imageurl": "dummylink"}

            resp = client.post("/users/new",
                               data=data,
                               follow_redirects=True)

            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Users</h1>", html)
            self.assertIn("<button>Add user</button>", html)
            self.assertIn("Jane Doe", html)

    def test_edit_user_redirect(self):
        """
        Test that editing a user results in a status code of 302 and redirects to the correct
        location.
        """

        with app.test_client() as client:
            data = {"firstname": "Jane",
                    "lastname": "Doe",
                    "imageurl": "dummylink"}

            resp = client.post(f"/users/{self.user0_id}/edit",
                               data=data,
                               follow_redirects=False)

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "/users")

    def test_edit_user_redirect_followed(self):
        """
        Test that editing a user results in a status code of 200 and redirects to a page with
        the appropriate content.
        """

        with app.test_client() as client:
            data = {"firstname": "Jane",
                    "lastname": "Doe",
                    "imageurl": "dummylink"}

            resp = client.post(f"/users/{self.user0_id}/edit",
                               data=data,
                               follow_redirects=True)

            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Users</h1>", html)
            self.assertIn("<button>Add user</button>", html)
            self.assertIn("Jane Doe", html)

    def test_delete_user_redirect(self):
        """
        Test that deleting a user results in a status code of 302 and redirects to the appropriate
        location.
        """

        with app.test_client() as client:
            resp = client.post(f"/users/{self.user0_id}/delete",
                               follow_redirects=False)

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "/users")

    def test_delete_user_redirect_followed(self):
        """
        Test that deleting a user results in a status code of 200 and redirects to a page with
        the appropriate content.
        """

        with app.test_client() as client:
            resp = client.post(f"/users/{self.user0_id}/delete",
                               follow_redirects=True)

            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Users</h1>", html)
            self.assertIn("<button>Add user</button>", html)

# -------------------------------------------------------------------------------------------------


# POST-RELATED TESTS ------------------------------------------------------------------------------
