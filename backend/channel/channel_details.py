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
def channel_details(token, channel_id):
	users = unbox('users', {})
	channels = unbox('channels', {})

	auth = users[str(decode(token)['u_id'])]

	channel = channels[str(channel_id)]

	if auth['u_id'] not in channel['all_members']:
		raise AccessError("Unauthorised")

	return {'name' : channel['name'],
		'owner_members': [{'u_id': u['u_id'], 'name_first': u['name_first'], 'name_last': u['name_last'], 'profile_img_url': u['profile_img_url']}
			for u in [users[str(id)] for id in channel['owner_members']]],
		'all_members': [{'u_id': u['u_id'], 'name_first': u['name_first'], 'name_last': u['name_last'], 'profile_img_url': u['profile_img_url']}
			for u in [users[str(id)] for id in channel['all_members']]]}
