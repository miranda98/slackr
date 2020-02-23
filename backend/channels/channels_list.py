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
def channels_list(token):
	users = unbox('users', {})
	channels = unbox('channels', {})

	auth = users[str(decode(token)['u_id'])]

	return {'channels': [{'channel_id': channels[id]['channel_id'], 'name': channels[id]['name']} for id in channels if auth['u_id'] in channels[id]['all_members']]}
