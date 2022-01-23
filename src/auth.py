from flask import Blueprint, redirect, render_template, url_for

auth = Blueprint("auth", __name__)


@auth.get("/login")
def login() -> str:
    return render_template("login.html")


@auth.get("/signup")
def signup() -> str:
    return render_template("signup.html")


@auth.get("/logout")
def logout():
    return redirect(url_for("views.homepage"))
