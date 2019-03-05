import os

from flask import Flask, session, redirect, abort, url_for, render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    # return "Project 1: TODO - HOME"
    return render_template("index.html")


@app.route("/book")
def book():
    return "Project 1: Books"


@app.route('/books/<int:book_id>')
def view_book(book_id):
    return "Project 1: Individual Book View - %d" % book_id


@app.route("/submit-review")
def submit_review():
    return "Project 1: Submit Review"


@app.route("/register")
def register():
    return "Project 1: Register"


@app.route("/login", methods=['GET', 'POST'])
def login():
    return "Project 1: Login"


@app.route("/logout")
def logout():
    return "Project 1: Logout"


@app.route("/search")
def search():
    return "Project 1: Search"


@app.route("/search/<string:query>")
def submit_search(query):
    return "Project 1: Searching for: %s" % query


@app.route("/api")
def api():
    return "Project 1: API"
