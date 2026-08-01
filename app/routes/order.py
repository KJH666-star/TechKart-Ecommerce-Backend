from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import db
from app.models.order import Order

order_bp = Blueprint("order", __name__)


@order_bp.route("/orders", methods=["POST"])
@jwt_required()
def create_order():

    data = request.get_json()

    order = Order(
        user_id=data["user_id"],
        total_amount=data["total_amount"]
    )

    db.session.add(order)
    db.session.commit()

    return jsonify({"message": "Order placed successfully"}), 201


@order_bp.route("/orders", methods=["GET"])
def get_orders():

    orders = Order.query.all()

    result = []

    for order in orders:
        result.append({
            "id": order.id,
            "user_id": order.user_id,
            "total_amount": order.total_amount,
            "status": order.status
        })

    return jsonify(result)


@order_bp.route("/orders/<int:id>", methods=["GET"])
def get_order(id):

    order = Order.query.get_or_404(id)

    return jsonify({
        "id": order.id,
        "user_id": order.user_id,
        "total_amount": order.total_amount,
        "status": order.status
    })