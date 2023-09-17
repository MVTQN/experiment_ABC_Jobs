from marshmallow import  Schema, fields
from sqlalchemy import Column, String, DateTime
from .model import Model, Base
import bcrypt
from datetime import datetime, timedelta
from uuid import uuid4

class User(Model, Base):
  __tablename__ = 'users'

  username = Column(String)
  email = Column(String)
  password = Column(String)
  

  def __init__(self, username, email, password):
    Model.__init__(self)
    self.username = username
    self.email = email
    
    password = password

class UserSchema(Schema):
  id = fields.Number()
  username = fields.Str()
  email = fields.Str()
  password = fields.Str()
  createdAt = fields.DateTime()

class UserJsonSchema(Schema):
  id = fields.Number()
  username = fields.Str()
  email = fields.Str()
  token = fields.Str()
  createdAt = fields.DateTime()
