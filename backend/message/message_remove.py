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
def message_remove(token, message_id):
	users = unbox('users', {})
	channels = unbox('channels', {})
	messages = unbox('messages', {})

	auth = users[str(decode(token)['u_id'])]
	message = messages[str(message_id)]
	channel = channels[str(message['channel_id'])]

	if message['u_id'] != auth['u_id'] and auth['permission_id'] == 3 and auth['u_id'] not in channel['owner_members']:
		raise AccessError("Unauthorised")

	del messages[str(message_id)]

	box('messages', messages)

	return {}
