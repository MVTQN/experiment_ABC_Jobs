from commands.get_user import GetUser
from commands.create_user import CreateUser
from session import Session, engine
from models.model import Base
from models.user import User
from errors.errors import IncompleteParams
from errors.errors import Unauthorized
from datetime import datetime, timedelta

class TestGetUser():
  def setup_method(self):
    Base.metadata.create_all(engine)
    self.session = Session()
    
    self.data = {
      'username': 'william',
      'email': 'william@gmail.com',
      'password': '123456'
    }
    self.user = CreateUser(self.data).execute()

  
  


  
  
  def teardown_method(self):
    self.session.close()
    Base.metadata.drop_all(bind=engine)