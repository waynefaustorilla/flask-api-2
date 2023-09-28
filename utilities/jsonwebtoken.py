from flask_jwt_extended import JWTManager

jsonwebtoken = JWTManager()

@jsonwebtoken.unauthorized_loader
def unauthorized_loader(callable):
  return { "message": "Unauthorized" }, 401