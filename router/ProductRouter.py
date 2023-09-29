from flask.views import MethodView
from flask_smorest import Blueprint
from flask_jwt_extended import jwt_required

ProductBlueprint = Blueprint("Products", __name__, description="Operations for Products")

@ProductBlueprint.route("")
class ProductList(MethodView):
  def get(self):
    return { "message": "Browse Products" }

  @jwt_required()
  def post(self):
    return { "message": "Add Product" }

@ProductBlueprint.route("/<string:store_id>")
class Product(MethodView):
  def get(self, store_id):
    return { "message": "Retrieve Product by ID" + store_id }

  @jwt_required()
  def put(self, store_id):
    return { "message": "Edit Product by ID" + store_id }

  @jwt_required()
  def delete(self, store_id):
    return { "message": "Delete Product by ID" + store_id }