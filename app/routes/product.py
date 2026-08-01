from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import db
from app.models.product import Product

product_bp = Blueprint("product", __name__)


# Create Product
@product_bp.route("/products", methods=["POST"])
@jwt_required()
def create_product():
    data = request.get_json()

    product = Product(
        name=data["name"],
        description=data["description"],
        price=data["price"],
        stock=data["stock"],
        image_url=data["image_url"]
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({"message": "Product added successfully"}), 201


# Get All Products
@product_bp.route("/products", methods=["GET"])
def get_products():

    products = Product.query.all()

    result = []

    for product in products:
        result.append({
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "stock": product.stock,
            "image_url": product.image_url
        })

    return jsonify(result), 200


# Get Single Product
@product_bp.route("/products/<int:id>", methods=["GET"])
def get_product(id):

    product = Product.query.get_or_404(id)

    return jsonify({
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "stock": product.stock,
        "image_url": product.image_url
    })


# Update Product
@product_bp.route("/products/<int:id>", methods=["PUT"])
@jwt_required()
def update_product(id):

    product = Product.query.get_or_404(id)

    data = request.get_json()

    product.name = data["name"]
    product.description = data["description"]
    product.price = data["price"]
    product.stock = data["stock"]
    product.image_url = data["image_url"]

    db.session.commit()

    return jsonify({"message": "Product Updated"})


# Delete Product
@product_bp.route("/products/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_product(id):

    product = Product.query.get_or_404(id)

    db.session.delete(product)

    db.session.commit()

    return jsonify({"message": "Product Deleted"})