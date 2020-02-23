from flask import Blueprint, request
from json import dumps

from . import (auth_login, auth_logout, auth_register,
	auth_passwordreset_request, auth_passwordreset_reset)

endpoints = Blueprint('auth', __name__)

@endpoints.route("/auth/login", methods=['POST'])
def endpoint_auth_login():
	email = str(request.form.get('email'))
	password = str(request.form.get('password'))

	return dumps(auth_login.auth_login(email, password))


@endpoints.route("/auth/logout", methods=['POST'])
def endpoint_auth_logout():
	token =  str(request.form.get('token'))

	return dumps(auth_logout.auth_logout(token))


@endpoints.route("/auth/register", methods=['POST'])
def endpoint_auth_register():
    email = str(request.form.get('email'))
    password = str(request.form.get('password'))
    name_first = str(request.form.get('name_first'))
    name_last = str(request.form.get('name_last'))

    return dumps(auth_register.auth_register(email, password, name_first, name_last))


@endpoints.route("/auth/passwordreset/request", methods=['POST'])
def endpoint_auth_passwordreset_request():
	email =  str(request.form.get('email'))

	return dumps(auth_passwordreset_request.auth_passwordreset_request(email))


@endpoints.route("/auth/passwordreset/reset", methods=['POST'])
def endpoint_auth_passwordreset_reset():
	reset_code = str(request.form.get('reset_code'))
	new_password = str(request.form.get('new_password'))

	return dumps(auth_passwordreset_reset.auth_passwordreset_reset(reset_code, new_password))
