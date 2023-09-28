from database import database
from datetime import datetime
from pytz import timezone

class Users(database.Model):
  __tablename__ = "users"

  id = database.Column(database.Integer, primary_key=True)
  firstname = database.Column(database.String(50), nullable=False)
  middlename = database.Column(database.String(50), nullable=True)
  lastname = database.Column(database.String(50), nullable=False)
  username = database.Column(database.String(20), nullable=False, unique=True)
  email = database.Column(database.String(100), nullable=False, unique=True)
  password = database.Column(database.String(255), nullable=False)
  date_created = database.Column(database.DateTime, default=datetime.utcnow().replace(tzinfo=timezone("UTC")).astimezone(timezone("Asia/Manila")))
  
  def __init__(self, firstname=None, middlename=None, lastname=None, username=None, email=None, password=None):
    self.firstname = firstname
    self.middlename = middlename
    self.lastname = lastname
    self.username = username
    self.email = email
    self.password = password
    self.date_created = datetime.utcnow()
    
  def set_firstname(self, firstname):
    self.firstname = firstname
    
  def set_middlename(self, middlename):
    self.middlename = middlename
    
  def set_lastname(self, lastname):
    self.lastname = lastname
    
  def set_username(self, username):
    self.username = username
    
  def set_email(self, email):
    self.email = email
    
  def set_password(self, password):
    self.password = password