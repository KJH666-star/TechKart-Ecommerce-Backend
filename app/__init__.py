from flask import Flask

from app.config import Config
from app.extensions import db, jwt, migrate
from app.models import User
from app.routes.auth import auth_bp


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    @app.route("/")
    def home():
        return {
            "message": "Welcome to TechKart E-Commerce Backend 🚀"
        }

    app.register_blueprint(auth_bp)

    return app