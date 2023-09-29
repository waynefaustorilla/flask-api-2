import os
from dotenv import load_dotenv
from dotenv import find_dotenv

load_dotenv(find_dotenv())

PROPAGATE_EXCEPTIONS = os.environ.get("PROPAGATE_EXCEPTIONS")
API_TITLE = os.environ.get("API_TITLE")
API_VERSION = os.environ.get("API_VERSION")
OPENAPI_VERSION = os.environ.get("OPENAPI_VERSION")
OPENAPI_URL_PREFIX = os.environ.get("OPENAPI_URL_PREFIX")
OPENAPI_SWAGGER_UI_PATH = os.environ.get("OPENAPI_SWAGGER_UI_PATH")
OPENAPI_SWAGGER_UI_URL = os.environ.get("OPENAPI_SWAGGER_UI_URL")
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")