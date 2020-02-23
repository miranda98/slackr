import os

from flask import Blueprint, request, send_from_directory
from json import dumps

from . import (user_profile, user_profile_setname, user_profile_setemail,
		user_profile_sethandle, user_profiles_uploadphoto)

endpoints = Blueprint('user', __name__)

@endpoints.route("/user/profile", methods=['GET'])
def endpoint_user_profile():
	token = str(request.args.get('token'))
	u_id = int(request.args.get('u_id'))

	return dumps(user_profile.user_profile(token, u_id))


@endpoints.route("/user/profile/setname", methods=['PUT'])
def endpoint_user_profile_setname():
	token = str(request.form.get('token'))
	name_first = str(request.form.get('name_first'))
	name_last = str(request.form.get('name_last'))

	return dumps(user_profile_setname.user_profile_setname(token, name_first, name_last))


@endpoints.route("/user/profile/setemail", methods=['PUT'])
def endpoint_user_profile_setemail():
	token = str(request.form.get('token'))
	email = str(request.form.get('email'))

	return dumps(user_profile_setemail.user_profile_setemail(token, email))


@endpoints.route("/user/profile/sethandle", methods=['PUT'])
def endpoint_user_profile_sethandle():
	token = str(request.form.get('token'))
	handle_str = str(request.form.get('handle_str'))

	return dumps(user_profile_sethandle.user_profile_sethandle(token, handle_str))


@endpoints.route("/user/profiles/uploadphoto", methods=['POST'])
def endpoint_user_profiles_uploadphoto():
	token = str(request.form.get('token'))
	img_url = str(request.form.get('img_url'))
	x_start = int(request.form.get('x_start'))
	y_start = int(request.form.get('y_start'))
	x_end = int(request.form.get('x_end'))
	y_end = int(request.form.get('y_end'))

	return dumps(user_profiles_uploadphoto.user_profiles_uploadphoto(token, img_url,
		x_start, y_start, x_end, y_end))

@endpoints.route('/user/profiles/photo/<path:path>', methods=['GET'])
def endpoint_user_profiles_photo(path):
	print(os.path.join(__file__, '../utility/storage'))
	return send_from_directory(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../utility/storage'), path)
