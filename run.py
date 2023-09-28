from app import create_app
from app import database

if __name__ == "__main__":
  app = create_app("./config.py")

  with app.app_context():
    database.create_all()

  app.run(debug=True)