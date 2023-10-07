from session import Session, engine
from models.model import Base
from models.user import User
from application import application
from commands.create_user import CreateUser
import json
from datetime import datetime, timedelta

class TestUsers():
  def setup_method(self):
    Base.metadata.create_all(engine)
    self.session = Session()

  def test_create_user(self):
    with application.test_client() as test_client:
      response = test_client.post(
        '/users', json={
          'username': 'William',
          'password': '123456',
          'email': 'william@gmail.com'
        }
      )
      response_json = json.loads(response.data)

      assert response.status_code == 201
      assert 'id' in response_json
      assert 'createdAt' in response_json

  def test_create_user_already_exists(self):
    data = {
      'username': 'William',
      'password': '123456',
      'email': 'william@gmail.com'
    }
    CreateUser(data).execute()

    with application.test_client() as test_client:
      response = test_client.post(
        '/users', json=data
      )

      assert response.status_code == 412

 
  def teardown_method(self):
    self.session.close()
    Base.metadata.drop_all(bind=engine)