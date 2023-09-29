from flask import Flask
from flask_smorest import Api

from router.StoreRouter import StoreBlueprint
from router.UserRouter import UserBlueprint
from router.ProductRouter import ProductBlueprint
from router.AuthRouter import AuthBlueprint

from database import database
from utilities.jsonwebtoken import jsonwebtoken

def create_app(config_filename):
  app = Flask(__name__)

  app.config.from_pyfile(config_filename)

  database.init_app(app)
  jsonwebtoken.init_app(app)

  api = Api(app)

  api.register_blueprint(AuthBlueprint, url_prefix="/api/v1/auth")
  api.register_blueprint(StoreBlueprint, url_prefix="/api/v1/stores")
  api.register_blueprint(UserBlueprint, url_prefix="/api/v1/users")
  api.register_blueprint(ProductBlueprint, url_prefix="/api/v1/products")
  
  return app