from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint("main", __name__)


@bp.route("/")
def home():
    return render_template("index.html")


@bp.route("/log", methods=["POST"])
def log_entry():
    # Handle form submission and save to database
    # Redirect or render a page as needed
    return redirect(url_for("main.home"))


@bp.route("/dashboard")
def dashboard():
    # Retrieve data from the database and render it
    return render_template("dashboard.html")
