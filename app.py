# Ioana A Mititean
# Unit 23 Exercise - Blogly App

"""
Blogly application - Flask setup and routes.
"""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, PLACEHOLDER_IMG

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config["SECRET_KEY"] = "O secreta foarte secreta"
debug = DebugToolbarExtension(app)

with app.app_context():
    db.create_all()


@app.route("/")
def homepage():
    """
    Blogly app homepage.
    Redirects to list of current users (/users).
    """

    return redirect("/users")


@app.route("/users")
def list_users():
    """
    Display list of current users and an 'add user' button.
    """

    users = User.query.all()
    return render_template("list_users.jinja2", users=users)


@app.route("/users/new")
def display_add_user_form():
    """
    Display form to add a new user to Blogly app database.
    """

    return render_template("create_user.jinja2")


@app.route("/users/new", methods=["POST"])
def add_user():
    """
    Add new user to Blogly app database and redirect to /users (user list) page.
    """

    first_name = request.form["firstname"]
    last_name = request.form["lastname"]
    image_url = request.form["imageurl"]

    if not image_url:
        image_url = None

    new_user = User(first_name=first_name,
                    last_name=last_name,
                    image_url=image_url)

    db.session.add(new_user)
    db.session.commit()

    return redirect("/users")


@app.route("/users/<int:user_id>")
def display_user_details(user_id):
    """
    Show information about the user with the given ID, and buttons to edit or delete that user.
    """

    user = User.query.get_or_404(user_id)
    return render_template("user_details.jinja2", user=user)


@app.route("/users/<int:user_id>/edit")
def display_edit_form(user_id):
    """
    Display the edit page for the user with the given ID.
    """

    user = User.query.get_or_404(user_id)
    return render_template("edit_user.jinja2", user=user)


@app.route("/users/<int:user_id>/edit", methods=["POST"])
def edit_user(user_id):
    """
    Edit the user with the given ID and redirect to /users (user list) page.
    """

    first_name = request.form["firstname"]
    last_name = request.form["lastname"]
    image_url = request.form["imageurl"]

    user = User.query.get_or_404(user_id)
    user.first_name = first_name
    user.last_name = last_name
    user.image_url = image_url if image_url else PLACEHOLDER_IMG

    db.session.commit()

    return redirect("/users")


@app.route("/users/<int:user_id>/delete", methods=["POST"])
def delete_user(user_id):
    """
    Delete the user with the given ID and redirect to /users (user list) page.
    """

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=False)
