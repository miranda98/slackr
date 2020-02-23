""" Module Based Imports """
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))

from utility.storage import box, unbox
from utility.errors import ValueError, AccessError
from utility.security import encode, decode

""" Other Imports """

import re, hashlib, time, uuid

""" Implementation """

def auth_login(email, password):
	email_to_u_id = unbox('email_to_u_id', {})
	users = unbox('users', {})

	if not re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email):
		raise ValueError(f"Invalid email: '{email}'")

	if email not in email_to_u_id:
		raise ValueError(f"Invalid email: '{email}'")

	user = users[str(email_to_u_id[email])]

	if hashlib.sha256(password.encode()).hexdigest() != user['password']:
		raise ValueError(f"Invalid credentials")

	token = encode({'u_id': user['u_id'], 'timestamp': int(round(time.time()))})

	tokens = unbox('tokens', [])

	tokens.append(token)

	box('tokens', tokens)

	return { 'u_id' : user['u_id'], 'token' : token }
