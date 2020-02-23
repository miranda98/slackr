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
def channel_removeowner(token, channel_id, u_id):
	users = unbox('users', {})
	channels = unbox('channels', {})

	auth = users[str(decode(token)['u_id'])]
	user = users[str(u_id)]

	channel = channels[str(channel_id)]

	if auth['permission_id'] == 3 and auth['u_id'] not in channel['owner_members']:
		raise AccessError("Unauthorised")

	if user['u_id'] not in channel['owner_members']:
		raise ValueError("User not owner")

	channel['owner_members'].remove(u_id)
	channel['all_members'].remove(u_id)

	channels[str(channel_id)] = channel

	box('channels', channels)

	return {}
