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

@Secured
@Identified
def message_send(token, channel_id, message):
	users = unbox('users', {})
	channels = unbox('channels', {})
	messages = unbox('messages', {})

	auth = users[str(decode(token)['u_id'])]
	channel = channels[str(channel_id)]

	if auth['u_id'] not in channel['all_members']:
		raise AccessError("Unauthorised")

	if not (1 <= len(message) <= 1000):
		raise ValueError("Message is either too long or too short")

	message_id = 0 if len(messages) == 0 else max([int(id) for id in messages]) + 1

	messages[str(message_id)] = {
		'message_id': message_id,
		'channel_id': channel_id,
		'u_id': auth['u_id'],
		'message': message,
		'time_created': int(time.time()),
		'reacts': {},
		'is_pinned': False
	}

	box('messages', messages)

	return { 'message_id': message_id }
