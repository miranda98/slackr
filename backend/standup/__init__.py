from flask import Blueprint, request
from json import dumps

from . import (standup_start, standup_active, standup_send)

endpoints = Blueprint('standup', __name__)

@endpoints.route("/standup/start", methods=['POST'])
def endpoint_standup_start():
	token = str(request.form.get('token'))
	channel_id = int(request.form.get('channel_id'))
	length = int(request.form.get('length'))

	return dumps(standup_start.standup_start(token, channel_id, length))

@endpoints.route("/standup/active", methods=['GET'])
def endpoint_standup_active():
	token = str(request.args.get('token'))
	channel_id = int(request.args.get('channel_id'))

	return dumps(standup_active.standup_active(token, channel_id))

@endpoints.route("/standup/send", methods=['POST'])
def endpoint_standup_send():
	token = str(request.form.get('token'))
	channel_id = int(request.form.get('channel_id'))
	message = str(request.form.get('message'))

	return dumps(standup_send.standup_send(token, channel_id, message))
