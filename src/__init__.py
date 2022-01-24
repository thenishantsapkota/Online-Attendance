from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_toastr import Toastr
from flask_login import LoginManager
import logging

logger = logging.getLogger(__name__)

db = SQLAlchemy()
toastr = Toastr()
DATABASE_NAME = "database.db"


def create_app() -> Flask:
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_NAME}"

    db.init_app(app)
    toastr.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app: Flask) -> None:
    if not path.exists("src/" + DATABASE_NAME):
        db.create_all(app=app)
        logger.info("Database Initialized!")
