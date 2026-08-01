from app.extensions import db


class Cart(db.Model):
    __tablename__ = "cart"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, nullable=False)

    product_id = db.Column(db.Integer, nullable=False)

    quantity = db.Column(db.Integer, nullable=False)

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )