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
def user_profile_setemail(token, email):
	email_to_u_id = unbox('email_to_u_id', {})
	users = unbox('users', {})

	auth = users[str(decode(token)['u_id'])]

	if not re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email):
		raise ValueError(f"Invalid email: {email}")

	if email in email_to_u_id:
		raise ValueError("Email already in use")

	del email_to_u_id[auth['email']]

	auth['email'] = email
	email_to_u_id[email] = auth['u_id']

	# update users
	users[str(auth['u_id'])] = auth

	box('email_to_u_id', email_to_u_id)
	box('users', users)

	return {}
