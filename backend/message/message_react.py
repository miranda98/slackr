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
def message_react(token, message_id, react_id):
	users = unbox('users', {})
	channels = unbox('channels', {})
	messages = unbox('messages', {})

	auth = users[str(decode(token)['u_id'])]
	message = messages[str(message_id)]
	channel = channels[str(message['channel_id'])]

	if auth['u_id'] not in channel['all_members']:
		raise AccessError("Unauthorised")

	if react_id not in [1]:
		raise ValueError(f"Invalid ID: react_id - {react_id}")

	reacts = message['reacts']

	if str(react_id) in reacts and auth['u_id'] in reacts[str(react_id)]['u_ids']:
		raise ValueError("React already exists")

	if str(react_id) in reacts:
		reacts[str(react_id)]['u_ids'].append(auth['u_id'])
	else:
		reacts[str(react_id)] = {'react_id' : react_id, 'u_ids' : [auth['u_id']]}

	message['reacts'] = reacts
	messages[str(message_id)] = message

	box('messages', messages)

	return {}
