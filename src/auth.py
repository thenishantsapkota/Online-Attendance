<<<<<<< Updated upstream
import email
=======
from distutils.log import error
from nis import cat
>>>>>>> Stashed changes
from flask import (
    Blueprint,
    Response,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from flask_login import login_user, current_user, logout_user

auth = Blueprint("auth", __name__)


@auth.get("/login")
def login() -> str:
    return render_template("login.html", user=current_user)


@auth.post("/login")
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password, password):
            flash("Logged in successfully!", category="success")
            login_user(user, remember=True)
            return redirect(url_for("views.homepage"))
        else:
            flash("Incorrect Email or Password, Try Again!", category="error")
    else:
        flash("Email doesn't exist!", category="error")
    return render_template("login.html", user=current_user)
        

@auth.get("/signup")
def signup() -> str:
    return render_template("signup.html", user=current_user)


@auth.post("/signup")
def signup_post():
    email = request.form.get("email")
    full_name = request.form.get("name")
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")

    user = User.query.filter_by(email=email).first()
    if user:
        flash("Email already exists.", category="error")
    elif password1 != password2:
        flash("Passwords don't match!", category="error")
    elif len(password1) < 7:
        flash("Password is too short, keep the password above 7 characters.")
    else:
        new_user = User(
            email=email,
            password=generate_password_hash(password1, method="sha256"),
            full_name=full_name,
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        flash("Account created successfully!", category="success")
        return redirect(url_for("views.homepage"))

    return render_template("signup.html", user=current_user)




@auth.get("/logout")
def logout() -> Response:
    logout_user()
    flash("Logged out!", category="success")
    return redirect(url_for("views.homepage"))

    
