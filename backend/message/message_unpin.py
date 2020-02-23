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
def message_unpin(token, message_id):
	users = unbox('users', {})
	channels = unbox('channels', {})
	messages = unbox('messages', {})

	auth = users[str(decode(token)['u_id'])]
	message = messages[str(message_id)]
	channel = channels[str(message['channel_id'])]

	if not message['is_pinned']:
		raise ValueError("Message is not pinned")

	if auth['permission_id'] == 3 and auth['u_id'] not in channel['owner_members']:
		raise AccessError("Unauthorised")

	message['is_pinned'] = False
	messages[str(message_id)] = message

	box('messages', messages)

	return {}
