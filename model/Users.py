from database import database
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from pytz import timezone
from passlib.hash import pbkdf2_sha256

class Users(database.Model):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True)
  firstname = Column(String(50), nullable=False)
  middlename = Column(String(50), nullable=True)
  lastname = Column(String(50), nullable=False)
  username = Column(String(20), nullable=False, unique=True)
  email = Column(String(100), nullable=False, unique=True)
  password = Column(String(255), nullable=False)
  date_created = Column(DateTime, default=datetime.utcnow().replace(tzinfo=timezone("UTC")).astimezone(timezone("Asia/Manila")))
    
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
    self.password = pbkdf2_sha256.hash(password)