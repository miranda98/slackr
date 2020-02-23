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
def channels_create(token, name, is_public):
	users = unbox('users', {})
	channels = unbox('channels', {})

	auth = users[str(decode(token)['u_id'])]

	if auth['permission_id'] == 3:
		raise AccessError("Unauthorised")

	if len(name) > 20:
		raise ValueError("Invalid name (too long)")

	channel_id = 0 if len(channels) == 0 else max([int(id) for id in channels]) + 1

	channels[str(channel_id)] = {'channel_id': channel_id, 'name': name, 'is_public': is_public, 'all_members': [auth['u_id']], 'owner_members': [auth['u_id']]}

	box('channels', channels)

	return { 'channel_id' : channel_id}
