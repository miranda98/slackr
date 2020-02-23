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
def channel_join(token, channel_id):
	users = unbox('users', {})
	channels = unbox('channels', {})

	auth = users[str(decode(token)['u_id'])]

	channel = channels[str(channel_id)]

	if auth['u_id'] in channel['all_members']:
		raise ValueError("Already a member")

	if auth['permission_id'] == 3 and not channel['is_public']:
		raise AccessError("Unauthorised")

	channel['all_members'].append(auth['u_id'])

	channels[str(channel_id)] = channel

	box('channels', channels)

	return {}
