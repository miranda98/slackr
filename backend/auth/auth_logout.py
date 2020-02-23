""" Module Based Imports """
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))

from utility.storage import box, unbox
from utility.errors import ValueError, AccessError
from utility.security import encode, decode

""" Other Imports """

import re, hashlib, time, uuid

""" Implementation """

def auth_logout(token):
	tokens = unbox('tokens', [])

	is_success = False

	if token in tokens:
		is_success = True
		tokens.remove(token)

	return {'is_success' : is_success}
