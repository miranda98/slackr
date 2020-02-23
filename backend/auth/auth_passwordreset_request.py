""" Module Based Imports """
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))

from utility.storage import box, unbox
from utility.errors import ValueError, AccessError
from utility.security import encode, decode
from utility.mail import mail

""" Other Imports """

import re, hashlib, time, uuid

""" Implementation """

def auth_passwordreset_request(email):
	email_to_u_id = unbox('email_to_u_id', {})
	reset_code_to_u_id = unbox('reset_code_to_u_id', {})

	if email not in email_to_u_id:
		raise ValueError(f"Invalid Email: '{email}'")

	reset_code = hashlib.sha256((email + str(int(time.time()))).encode()).hexdigest()[:8]
	reset_code_to_u_id[reset_code] = email_to_u_id[email]

	box('reset_code_to_u_id', reset_code_to_u_id)

	mail(email, "Slackr: Password Reset", f"Please enter the following code to reset your password: {reset_code}")

	return {}
