from flask import Blueprint, request
from json import dumps

from . import (message_sendlater, message_send, message_remove, message_edit,
	message_react, message_unreact, message_pin, message_unpin)

endpoints = Blueprint('message', __name__)

@endpoints.route("/message/sendlater", methods=['POST'])
def endpoint_message_sendlater():
	token = str(request.form.get('token'))
	channel_id = int(request.form.get('channel_id'))
	message = str(request.form.get('message'))
	time_sent = int(float(request.form.get('time_sent')))

	return dumps(message_sendlater.message_sendlater(token, channel_id, message, time_sent))


@endpoints.route("/message/send", methods=['POST'])
def endpoint_message_send():
	token = str(request.form.get('token'))
	channel_id = int(request.form.get('channel_id'))
	message = str(request.form.get('message'))

	return dumps(message_send.message_send(token, channel_id, message))


@endpoints.route("/message/remove", methods=['DELETE'])
def endpoint_message_remove():
	token = str(request.form.get('token'))
	message_id = int(request.form.get('message_id'))

	return dumps(message_remove.message_remove(token, message_id))


@endpoints.route("/message/edit", methods=['PUT'])
def endpoint_message_edit():
	token = str(request.form.get('token'))
	message_id = int(request.form.get('message_id'))
	message = str(request.form.get('message'))

	return dumps(message_edit.message_edit(token, message_id, message))


@endpoints.route("/message/react", methods=['POST'])
def endpoint_message_react():
	token = str(request.form.get('token'))
	message_id = int(request.form.get('message_id'))
	react_id = int(request.form.get('react_id'))

	return dumps(message_react.message_react(token, message_id, react_id))

@endpoints.route("/message/unreact", methods=['POST'])
def endpoint_message_unreact():
	token = str(request.form.get('token'))
	message_id = int(request.form.get('message_id'))
	react_id = int(request.form.get('react_id'))

	return dumps(message_unreact.message_unreact(token, message_id, react_id))


@endpoints.route("/message/pin", methods=['POST'])
def endpoint_message_pin():
	token = str(request.form.get('token'))
	message_id = int(request.form.get('message_id'))

	return dumps(message_pin.message_pin(token, message_id))


@endpoints.route("/message/unpin", methods=['POST'])
def endpoint_message_unpin():
	token = str(request.form.get('token'))
	message_id = int(request.form.get('message_id'))

	return dumps(message_unpin.message_unpin(token, message_id))
