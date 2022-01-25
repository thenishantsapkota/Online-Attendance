from flask import Blueprint, render_template
from flask_login import current_user, login_required

views = Blueprint("views", __name__)


@views.get("/")
def homepage():
    return render_template("index.html", user=current_user)


@views.get("/profile")
@login_required
def profile():
    return render_template("profile.html", user=current_user)
