from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

class SessionConfig():
  def __init__(self):
    print('')

  def url(self):
    db_config = self.config()
    return 'sqlite:///conversion_system.db'
    #return f'postgresql://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}:{db_config["port"]}/{db_config["db"]}'
    
  def config(self):
    db_name = os.environ['DB_NAME'] if 'DB_NAME' in os.environ else 'monitor_users'
    if "ENV" in os.environ and os.environ['ENV'] == 'test':
      db_name += '_test'

    base_config = {
      'host': os.environ['DB_HOST'] if 'DB_HOST' in os.environ else 'localhost',
      'port': os.environ['DB_PORT'] if 'DB_PORT' in os.environ else '5432',
      'user': os.environ['DB_USER'] if 'DB_USER' in os.environ else 'postgres',
      'password': os.environ['DB_PASSWORD'] if 'DB_PASSWORD' in os.environ else 'postgres',
      'db': db_name
    }

    return base_config

session_config = SessionConfig()
engine = create_engine(session_config.url())
Session = sessionmaker(bind=engine)