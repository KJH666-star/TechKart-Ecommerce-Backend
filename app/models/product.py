from app.extensions import db


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(150), nullable=False)

    description = db.Column(db.Text)

    price = db.Column(db.Float, nullable=False)

    stock = db.Column(db.Integer, nullable=False, default=0)

    image_url = db.Column(db.String(500))

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )