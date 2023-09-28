from database import database

class Products(database.Model):
  __tablename__ = "products"

  id = database.Column(database.Integer, primary_key=True)
  name = database.Column(database.String(80), unique=True, nullable=False)
  price = database.Column(database.Float(precision=2), unique=False, nullable=False)
  store_id = database.Column(database.Integer, database.ForeignKey("stores.id"), unique=False, nullable=False)
  store = database.relationship("Stores", back_populates="products")