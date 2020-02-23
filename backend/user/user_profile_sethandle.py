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
def user_profile_sethandle(token, handle_str):
	handle_to_u_id = unbox('handle_to_u_id', {})
	users = unbox('users', {})

	if not (3 <= len(handle_str) <= 20):
		raise ValueError("Handle too long or too short")

	if handle_str in handle_to_u_id:
		raise ValueError("Handle already in use")

	auth = users[str(decode(token)['u_id'])]

	del handle_to_u_id[auth['handle_str']]

	auth['handle_str'] = handle_str
	handle_to_u_id[handle_str] = auth['u_id']

	users[str(auth['u_id'])] = auth

	box('handle_to_u_id', handle_to_u_id)
	box('users', users)

	return {}
