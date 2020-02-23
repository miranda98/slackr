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

from message import message_send

@Secured
@Identified
def standup_start(token, channel_id, length):
	users = unbox('users', {})
	channels = unbox('channels', {})
	channel_id_to_time_finish = unbox('channel_id_to_time_finish', {})
	channel_id_to_messages = unbox('channel_id_to_messages', {})

	auth = users[str(decode(token)['u_id'])]
	channel = channels[str(channel_id)]

	if str(channel_id) in channel_id_to_time_finish:
		raise ValueError("Standup already started")

	time_finish = int(time.time()) + length
	channel_id_to_time_finish[str(channel_id)] = time_finish
	channel_id_to_messages[str(channel_id)] = []

	box('channel_id_to_messages', channel_id_to_messages)
	box('channel_id_to_time_finish', channel_id_to_time_finish)

	timer = Timer(length, _delay, args=[token, channel_id], kwargs=None)
	timer.start()

	return { 'time_finish': time_finish }

def _delay(token, channel_id):
	channel_id_to_time_finish = unbox('channel_id_to_time_finish', {})
	channel_id_to_messages = unbox('channel_id_to_messages', {})

	users = unbox('users', {})

	message = "\n".join([users[str(m['u_id'])]['handle_str'] + ': ' + m['message'] for m in channel_id_to_messages[str(channel_id)]])

	message_send.message_send(token, channel_id, message)

	del channel_id_to_time_finish[str(channel_id)]
	del channel_id_to_messages[str(channel_id)]

	box('channel_id_to_time_finish', channel_id_to_time_finish)
	box('channel_id_to_messages', channel_id_to_messages)
