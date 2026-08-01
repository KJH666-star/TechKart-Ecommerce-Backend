from flask import Flask
from app.routes.product import product_bp
from app.config import Config
from app.extensions import db, jwt, migrate
from app.models import User
from app.routes.auth import auth_bp
from app.models.category import Category
from app.routes.category import category_bp
from app.models.cart import Cart
from app.routes.cart import cart_bp
from app.models.order import Order
from app.routes.order import order_bp
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
    app.register_blueprint(product_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(order_bp)
    return app