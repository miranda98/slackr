""" Module Based Imports """
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))

from utility.storage import box, unbox
from utility.errors import ValueError, AccessError
from utility.security import encode, decode

""" Other Imports """

import re, hashlib, time, uuid

""" Implementation """

def auth_passwordreset_reset(reset_code, new_password):
	users = unbox('users', {})
	reset_code_to_u_id = unbox('reset_code_to_u_id', {})

	if reset_code not in reset_code_to_u_id:
		raise ValueError(f"Invalid reset code: '{reset_code}'")

	if len(new_password) < 6:
		raise ValueError("Invalid new password")

	user = users[str(reset_code_to_u_id[reset_code])]

	del reset_code_to_u_id[reset_code]

	user['password'] = hashlib.sha256(new_password.encode()).hexdigest()
	users[user['u_id']] = user

	box('reset_code_to_u_id', reset_code_to_u_id)
	box('users', users)

	return {}
