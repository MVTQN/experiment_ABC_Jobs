from .base_command import BaseCommannd
from models.user import User, UserSchema, UserJsonSchema
from session import Session
from errors.errors import IncompleteParams, UserAlreadyExists
from sqlalchemy import or_

class CreateUser(BaseCommannd):
  def __init__(self, data):
    self.data = data
  
  def execute(self):
    try:
      posted_user = UserSchema(
        only=('username', 'email', 'password')
      ).load(self.data)
      user = User(**posted_user)
      session = Session()
      
      if self.username_exist(session, self.data['username']) or self.email_exist(session, self.data['email']):
        session.close()
        raise UserAlreadyExists()

      session.add(user)
      session.commit()

      new_user = UserJsonSchema().dump(user)
      session.close()

      return new_user
    except TypeError:
      raise IncompleteParams()
  
  def username_exist(self, session, username):
    return len(session.query(User).filter_by(username=username).all()) > 0

  def email_exist(self, session, email):
    return len(session.query(User).filter_by(email=email).all()) > 0