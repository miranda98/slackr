from flask import Blueprint, request
from json import dumps

from . import (channel_invite, channel_details, channel_messages,
	channel_leave, channel_join, channel_addowner, channel_removeowner)

endpoints = Blueprint('channel', __name__)

@endpoints.route("/channel/invite", methods=['POST'])
def endpoint_channel_invite():
	token = str(request.form.get('token'))
	channel_id = int(request.form.get('channel_id'))
	u_id = int(request.form.get('u_id'))

	return dumps(channel_invite.channel_invite(token, channel_id, u_id))


@endpoints.route("/channel/details", methods=['GET'])
def endpoint_channel_details():
	token = str(request.args.get('token'))
	channel_id = int(request.args.get('channel_id'))

	return dumps(channel_details.channel_details(token, channel_id))


@endpoints.route("/channel/messages", methods=['GET'])
def endpoint_channel_messages():
	token = str(request.args.get('token'))
	channel_id = int(request.args.get('channel_id'))
	start = int(request.args.get('start'))

	return dumps(channel_messages.channel_messages(token, channel_id, start))


@endpoints.route("/channel/leave", methods=['POST'])
def endpoint_channel_leave():
	token = str(request.form.get('token'))
	channel_id = int(request.form.get('channel_id'))

	return dumps(channel_leave.channel_leave(token, channel_id))


@endpoints.route("/channel/join", methods=['POST'])
def endpoint_channel_join():
	token = str(request.form.get('token'))
	channel_id = int(request.form.get('channel_id'))

	return dumps(channel_join.channel_join(token, channel_id))


@endpoints.route("/channel/addowner", methods=['POST'])
def endpoint_channel_addowner():
	token = str(request.form.get('token'))
	channel_id = int(request.form.get('channel_id'))
	u_id = int(request.form.get('u_id'))

	return dumps(channel_addowner.channel_addowner(token, channel_id, u_id))


@endpoints.route("/channel/removeowner", methods=['POST'])
def endpoint_channel_removeowner():
	token = str(request.form.get('token'))
	channel_id = int(request.form.get('channel_id'))
	u_id = int(request.form.get('u_id'))

	return dumps(channel_removeowner.channel_removeowner(token, channel_id, u_id))
