from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.extensions import db
from app.models.category import Category

category_bp = Blueprint("category", __name__)


# Create Category
@category_bp.route("/categories", methods=["POST"])
@jwt_required()
def create_category():
    data = request.get_json()

    category = Category(
        name=data["name"]
    )

    db.session.add(category)
    db.session.commit()

    return jsonify({"message": "Category Added Successfully"}), 201


# Get All Categories
@category_bp.route("/categories", methods=["GET"])
def get_categories():

    categories = Category.query.all()

    result = []

    for category in categories:
        result.append({
            "id": category.id,
            "name": category.name
        })

    return jsonify(result)


# Get Category by ID
@category_bp.route("/categories/<int:id>", methods=["GET"])
def get_category(id):

    category = Category.query.get_or_404(id)

    return jsonify({
        "id": category.id,
        "name": category.name
    })


# Update Category
@category_bp.route("/categories/<int:id>", methods=["PUT"])
@jwt_required()
def update_category(id):

    category = Category.query.get_or_404(id)

    data = request.get_json()

    category.name = data["name"]

    db.session.commit()

    return jsonify({"message": "Category Updated"})


# Delete Category
@category_bp.route("/categories/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_category(id):

    category = Category.query.get_or_404(id)

    db.session.delete(category)

    db.session.commit()

    return jsonify({"message": "Category Deleted"})