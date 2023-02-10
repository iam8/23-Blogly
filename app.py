# Ioana A Mititean
# Unit 23 Exercise - Blogly App

"""
Blogly application - Flask setup and routes.
"""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, PLACEHOLDER_IMG

app = Flask(__name__)

app.config["SECRET_KEY"] = "O secreta foarte secreta"
debug = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_ECHO'] = True

app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False


@app.route("/")
def homepage():
    """
    Blogly app homepage.
    Redirects to list of current users (/users).
    """

    return redirect("/users")


# USER-RELATED ROUTES -----------------------------------------------------------------------------

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
def display_user_edit_form(user_id):
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

# -------------------------------------------------------------------------------------------------


# POST-RELATED ROUTES -----------------------------------------------------------------------------

@app.route("/users/<int:user_id>/posts/new")
def display_add_post_form(user_id):
    """
    Display form to create and add a new post for the given user.
    """

    return render_template("create_post.jinja2")


@app.route("/users/<int:user_id>/posts/new", methods=["POST"])
def add_post(user_id):
    """
    Add new post to Blogly app database for the given user and redirect to the details page for
    that user.
    """


@app.route("/posts/<int:post_id>")
def display_post_details(post_id):
    """
    Show information about the post with the given ID, and buttons to edit or delete that post.
    """


@app.route("/posts/<int:post_id>/edit")
def display_post_edit_form(post_id):
    """
    Display the edit page for the post with the given ID.
    """


@app.route("/posts/<int:post_id>/edit", methods=["POST"])
def edit_post(post_id):
    """
    Edit the post with the given ID and redirect to the details page for that post.
    """


@app.route("/posts/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    """
    Delete the post with the given ID and redirect to /users (user list) page.
    """

# -------------------------------------------------------------------------------------------------


if __name__ == "__main__":

    connect_db(app)

    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port=5000, debug=True, threaded=False)
