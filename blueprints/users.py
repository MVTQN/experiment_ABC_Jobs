from flask import Flask, jsonify, request, Blueprint
from commands.create_user import CreateUser

from commands.get_user import GetUser


users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users', methods = ['POST'])
def create():
    user = CreateUser(request.get_json()).execute()
    return jsonify(user), 201


@users_blueprint.route('/users/reset', methods = ['POST'])
def reset():
    Reset().execute()
    return jsonify({'status': 'OK'})

