from flask import make_response
from flask.views import MethodView
from flask_smorest import Blueprint
from flask_smorest import abort
from utilities.bcrypt import bcrypt
from schema.AuthSchema import AuthSchema
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from model.Users import Users

AuthBlueprint = Blueprint("Auth", __name__, description="Operations for Auth")

@AuthBlueprint.route("/login")
class Login(MethodView):
  @AuthBlueprint.arguments(AuthSchema)
  def post(self, validated):
    user = Users.query.filter_by(username=validated["username"]).first()

    if not user:
      abort(400, "Invalid Username or Password")

    if not bcrypt.check_password_hash(user.password, validated["password"]):
      print("Here!")
      return abort(400, "Invalid Username or Password")

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)

    response = make_response({ "access_token": access_token })

    response.set_cookie("refresh_token", refresh_token, httponly=True, secure=True)

    return response

@AuthBlueprint.route("/logout")
class Logout(MethodView):
  def post(self):
    return { "message": "Logout Successful" }