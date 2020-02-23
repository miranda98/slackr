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
def standup_send(token, channel_id, message):
	users = unbox('users', {})
	channels = unbox('channels', {})
	channel_id_to_time_finish = unbox('channel_id_to_time_finish', {})
	channel_id_to_messages = unbox('channel_id_to_messages', {})

	auth = users[str(decode(token)['u_id'])]
	channel = channels[str(channel_id)]

	if str(channel_id) not in channel_id_to_time_finish:
		raise ValueError("No standup has been started")

	if auth['u_id'] not in channel['all_members']:
		raise AccessError("Unauthorised")

	if not (1 <= len(message) <= 1000):
		raise ValueError("Message too long or too short")

	channel_id_to_messages[str(channel_id)].append({'u_id': auth['u_id'], 'message': message})

	box('channel_id_to_messages', channel_id_to_messages)

	return {}
