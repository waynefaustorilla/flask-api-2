from flask.views import MethodView
from flask_smorest import Blueprint
from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import jwt_required

from model.Users import Users
from schema.UserSchema import UserSchema, UserUpdateSchema
from database import database

UserBlueprint = Blueprint("Users", __name__, description="Operations for Users")

@UserBlueprint.route("")
class StoreList(MethodView):
  @UserBlueprint.response(200, UserSchema(many=True))
  def get(self):
    users = Users.query.all()
    
    return users

  @UserBlueprint.arguments(UserSchema)
  def post(self, validated):
    if validated["password"] != validated["repeat_password"]:
      abort(400, message="Passwords Do Not Match")

    try:
      user = Users()

      user.set_firstname(validated["firstname"])
      user.set_middlename(validated["middlename"])
      user.set_lastname(validated["lastname"])
      user.set_username(validated["username"])
      user.set_email(validated["email"])
      user.set_password(validated["password"])

      database.session.add(user)
      database.session.commit()

      return { "message": "User Created Successfully" }, 201
    except SQLAlchemyError as error:
      print(error)

      abort(500, message="Something Went Wrong")

@UserBlueprint.route("/<string:username>")
class Store(MethodView):
  @UserBlueprint.response(200, UserSchema)
  def get(self, username):
    return self.findOrFail(username)

  @UserBlueprint.arguments(UserUpdateSchema)
  @UserBlueprint.response(200, UserSchema)
  @jwt_required()
  def put(self, validated, username):
    user = self.findOrFail(username)

    for key, value in validated.items():
      setattr(user, key, value)

    try:
      database.session.add(user)
      database.session.commit()

      return user, 200
    except SQLAlchemyError:
      abort(409, "Username is Already Taken")

  @jwt_required()
  def delete(self, username):
    user = self.findOrFail(username)

    database.session.delete(user)
    database.session.commit()

    return { "message": "User Deleted Successfully" }

  def findOrFail(self, username):
    user = Users.query.filter_by(username=username).first()

    if not user:
      abort(404, "User Not Found")

    return user