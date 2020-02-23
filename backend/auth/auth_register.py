""" Module Based Imports """
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))

from utility.storage import box, unbox
from utility.errors import ValueError, AccessError
from utility.security import encode, decode

""" Other Imports """

import re, hashlib, time, uuid

""" Implementation """

from . import auth_login

def auth_register(email, password, name_first, name_last):
	email_to_u_id = unbox('email_to_u_id', {})
	handle_to_u_id = unbox('handle_to_u_id', {})
	users = unbox('users', {})

	if not re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email):
		raise ValueError(f"Invalid email: '{email}'")

	if email in email_to_u_id:
		raise ValueError("Email already in use")

	if len(password) < 6:
		raise ValueError("Invalid password")

	if not (1 < len(name_first) < 50):
		raise ValueError("First name too short")

	if not (1 < len(name_last) < 50):
		raise ValueError("Last name too short")

	handle_str = name_first.lower() + name_last.lower()

	if len(handle_str) > 20:
		handle_str = handle_str[0:20]

	if handle_str in handle_to_u_id:
		handle_str = handle_str + str(len(handle_to_u_id))

	u_id = 0 if not users else max([int(id) for id in users]) + 1

	handle_to_u_id[handle_str] = u_id
	email_to_u_id[email] = u_id

	profile_img_url = unbox('url_base', '') + '/user/profiles/photo/default.jpg'

	users[str(u_id)] = {
		'u_id' : u_id,
		'email' : email,
		'password' : hashlib.sha256(password.encode()).hexdigest(),
		'permission_id' : 1 if u_id == 0 else 3,
		'profile_img_url' : profile_img_url,
		'name_first' : name_first,
		'name_last' : name_last,
		'handle_str' : handle_str
	}

	box('handle_to_u_id', handle_to_u_id)
	box('email_to_u_id', email_to_u_id)
	box('users', users)

	return auth_login.auth_login(email, password)
