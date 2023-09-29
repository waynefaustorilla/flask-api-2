from flask_jwt_extended import JWTManager

jsonwebtoken = JWTManager()

@jsonwebtoken.unauthorized_loader
def unauthorized_loader(callback):
  return { "message": "Unauthorized" }, 401

@jsonwebtoken.expired_token_loader
def expired_token_callback(header, payload):
  return { "message": "Session expired" }, 401

@jsonwebtoken.invalid_token_loader
def invalid_token_callback(error):
  return { "message": "Invalid Token" }, 401