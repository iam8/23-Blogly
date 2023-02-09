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
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

app.config["SECRET_KEY"] = "O secreta foarte secreta"
debug = DebugToolbarExtension(app)

with app.app_context():
    db.create_all()


@app.route("/")
def homepage():
    """
    Blogly app homepage - shows list of current users and an 'add user' button.
    """

    users = User.query.all()
    return render_template("home.jinja2", users=users)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=False)
