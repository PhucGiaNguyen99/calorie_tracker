from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import FoodEntry, ExerciseEntry

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
    food_entries = FoodEntry.query.all()
    exercise_entries = ExerciseEntry.query.all()
    return render_template(
        "dashboard.html", food_entries=food_entries, exercise_entries=exercise_entries
    )


@bp.route("/add_food", methods=["POST"])
def add_food():
    name = request.form.get("name")
    calories = request.form.get("calories")

    if name and calories:
        food_entry = FoodEntry(name=name, calories=calories)
        db.session.add(food_entry)
        db.session.commit()

    return redirect(url_for("main.dashboard"))


@bp.route("/add_exercise", methods=["POST"])
def add_exercise():
    name = request.form.get("name")
    calories_burned = request.form.get("calories_burned")

    if name and calories_burned:
        exercise_entry = ExerciseEntry(name=name, calories_burned=calories_burned)
        db.session.add(exercise_entry)
        db.session.commit()

    return redirect(url_for("main.dashboard"))
