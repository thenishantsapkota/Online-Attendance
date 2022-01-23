from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging

logger = logging.getLogger(__name__)

db = SQLAlchemy()
DATABASE_NAME = "database.db"


def create_app() -> Flask:
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_NAME}"

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    create_database(app)

    return app


def create_database(app: Flask) -> None:
    if not path.exists("src/" + DATABASE_NAME):
        db.create_all(app=app)
        logger.info("Database Initialized!")
