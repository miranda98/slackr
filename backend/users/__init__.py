from flask import Blueprint, request
from json import dumps

from . import users_all

endpoints = Blueprint('users', __name__)

@endpoints.route("/users/all", methods=['GET'])
def endpoint_users_all():
	token = str(request.args.get('token'))

	return dumps(users_all.users_all(token))
