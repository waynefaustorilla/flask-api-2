from database import database

class Stores(database.Model):
  __tablename__ = "stores"

  id = database.Column(database.Integer, primary_key=True)
  name = database.Column(database.String(80), nullable=False)
  products = database.relationship("Products", back_populates="store", lazy="dynamic")