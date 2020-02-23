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
def user_profile_setname(token, name_first, name_last):
	if not (1 < len(name_first) < 50):
		raise ValueError("First name too short")

	if not (1 < len(name_last) < 50):
		raise ValueError("Last name too short")

	users = unbox('users', {})
	auth = users[str(decode(token)['u_id'])]

	auth['name_first'] = name_first
	auth['name_last'] = name_last

	users[str(auth['u_id'])] = auth

	box('users', users)

	return {}
