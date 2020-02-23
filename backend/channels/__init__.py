from flask import Blueprint, request
from json import dumps

from . import (channels_list, channels_listall, channels_create)

endpoints = Blueprint('channels', __name__)

@endpoints.route("/channels/list", methods=['GET'])
def endpoint_channels_list():
	token = str(request.args.get('token'))

	return dumps(channels_list.channels_list(token))


@endpoints.route("/channels/listall", methods=['GET'])
def endpoint_channels_listall():
	token = str(request.args.get('token'))

	return dumps(channels_listall.channels_listall(token))


@endpoints.route("/channels/create", methods=['POST'])
def endpoint_channels_create():
	token = str(request.form.get('token'))
	name = str(request.form.get('name'))
	is_public = request.form.get('is_public') != 'false'

	return dumps(channels_create.channels_create(token, name, is_public))
