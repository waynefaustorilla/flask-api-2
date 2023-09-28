from flask import Flask
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
from flask_smorest import abort
from database import database
from model.Stores import Stores

StoreBlueprint = Blueprint("Stores", __name__, description="Operations for Store")

@StoreBlueprint.route("")
class StoreList(MethodView):
  def get(self):
    stores = Stores.query.all()
    
    return { "stores": stores }

  def post(self):
    try:
      request_body = request.get_json()
      
      new_store = Stores(**request_body)
      
      database.session.add(new_store)
      database.session.commit()
      
      return { "store": new_store }, 201
    except Exception as exception:
      print(exception)
      
      abort(500, message="Something Went Wrong")

@StoreBlueprint.route("/<string:store_id>")
class Store(MethodView):
  def get(self, store_id):
    try:
      store = Stores.query.filter_by(id=store_id).first()
      
      return store
    except Exception:
      abort(404, message="Store Not Found")

  def put(self, store_id):
    return { "message": "Edit Store by ID" + store_id }

  def delete(self, store_id):
    return { "message": "Delete Store by ID" + store_id }