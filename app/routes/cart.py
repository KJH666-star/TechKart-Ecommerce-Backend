from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import db
from app.models.cart import Cart

cart_bp = Blueprint("cart", __name__)


@cart_bp.route("/cart", methods=["POST"])
@jwt_required()
def add_to_cart():

    data = request.get_json()

    cart = Cart(
        user_id=data["user_id"],
        product_id=data["product_id"],
        quantity=data["quantity"]
    )

    db.session.add(cart)
    db.session.commit()

    return jsonify({"message": "Product added to cart"}), 201


@cart_bp.route("/cart", methods=["GET"])
def get_cart():

    items = Cart.query.all()

    result = []

    for item in items:
        result.append({
            "id": item.id,
            "user_id": item.user_id,
            "product_id": item.product_id,
            "quantity": item.quantity
        })

    return jsonify(result)


@cart_bp.route("/cart/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_cart(id):

    item = Cart.query.get_or_404(id)

    db.session.delete(item)

    db.session.commit()

    return jsonify({"message": "Item removed"})