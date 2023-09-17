from flask import Flask, jsonify
from session import Session, engine
from models.model import Base
from blueprints.users import users_blueprint
from errors.errors import ApiError

application= Flask(__name__)
application.register_blueprint(users_blueprint)

Base.metadata.create_all(engine)

@application.errorhandler(ApiError)
def handle_exception(err):
    response = {
      "mssg": err.description 
    }
    return jsonify(response), err.code
if __name__ == "__main__":
    application.run(port = 5000, debug = True)
