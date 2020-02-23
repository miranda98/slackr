""" Module Based Imports """
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))

from utility.storage import box, unbox
from utility.errors import ValueError, AccessError
from utility.security import encode, decode
from utility.wrappers import Virtualized, Secured, Identified

""" Other Imports """

import re, hashlib, time, uuid

""" Implementation """

from threading import Timer

from . import message_send

@Secured
@Identified
def message_sendlater(token, channel_id, message, time_sent):
	users = unbox('users', {})
	channels = unbox('channels', {})
	messages = unbox('messages', {})

	auth = users[str(decode(token)['u_id'])]
	channel = channels[str(channel_id)]

	if auth['u_id'] not in channel['all_members']:
		raise AccessError("Unauthorised")

	if not (1 <= len(message) <= 1000):
		raise ValueError("Message is either too long or too short")

	nowish = int(time.time())

	if time_sent < nowish:
		raise ValueError("Time to send is in the past")

	message_id = 0 if len(messages) == 0 else max([int(id) for id in messages]) + 1

	messages[str(message_id)] = {
		'message_id': message_id,
		'channel_id': None,
		'u_id': None,
		'message': message,
		'time_created': time_sent,
		'reacts': {},
		'is_pinned': False
	}

	box('messages', messages)

	timer = Timer(time_sent - nowish, _delayed, args=[auth['u_id'], message_id, channel_id], kwargs=None)
	timer.start()

	return { 'message_id': message_id }

def _delayed(u_id, message_id, channel_id):
	messages = unbox('messages', {})
	messages[str(message_id)]['u_id'] = u_id
	messages[str(message_id)]['channel_id'] = channel_id
	box('messages', messages)
