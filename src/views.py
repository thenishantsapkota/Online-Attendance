from flask import Blueprint, render_template

views = Blueprint("views", __name__)


@views.get("/")
def homepage():
    return render_template("index.html")
