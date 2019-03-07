#!/Users/rxnin/.environments/cs50/bin/python

import os

from flask import Flask, session, redirect, abort, url_for, render_template, flash
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from forms import RegistrationForm, LoginForm

app = Flask(__name__)


# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = "a8f388bf05805c8a156ca7987919cc0e"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# bcrypt = Bcrpyt(app)

books = []


@app.route("/", methods=["GET", "POST"])
def index():
    # return "Project 1: TODO - HOME"
    pageTitle = "Home"
    return render_template("index.html", pageTitle=pageTitle)


@app.route("/about")
def about():
    # return "Project 1: TODO - HOME"
    pageTitle = "About"
    return render_template("about.html", pageTitle=pageTitle)


@app.route("/book")
def book():
    pageTitle = "Book View"
    return "Project 1: Books"


@app.route('/books/<int:book_id>')
def view_book(book_id):
    pageTitle = "Individual Book Page View"
    return "Project 1: Individual Book View - %d" % book_id


@app.route("/submit-review")
def submit_review():
    pageTitle = "Submit Review"
    return "Project 1: Submit Review"


@app.route("/register", methods=['POST', 'GET'])
def register():
    pageTitle = "Registration View"
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('index'))
    # return "Project 1: Register"
    return render_template("auth/register.html", pageTitle=pageTitle, form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    pageTitle = "Login to your Account"
    # return "Project 1: Login"
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('auth/login.html', title=pageTitle, form=form)


@app.route("/logout")
def logout():
    pageTitle = "Logout"
    return "Project 1: Logout"


@app.route("/search")
def search():
    pageTitle = "Search"
    return "Project 1: Search"


@app.route("/search/<string:query>", methods=['GET', 'POST'])
def submit_search(query):
    pageTitle = "Search query"
    return "Project 1: Searching for: %s" % query


@app.route("/api")
def api():
    pageTitle = "API Access"
    return "Project 1: API"
