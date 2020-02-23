""" Module Based Imports """
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))

from utility.storage import box, unbox
from utility.errors import ValueError, AccessError
from utility.security import encode, decode
from utility.wrappers import Virtualized

""" Other Imports """

import re, hashlib, time, uuid

""" Implementation """

import pytest

from . import auth_login

PASSWORD = "secret"
HASH = hashlib.sha256(PASSWORD.encode()).hexdigest()

@Virtualized
def test_auth_login_invalid_email():
	box('tokens', [])
	box('users', {"1" : { "u_id": 1, "email": "jane.citizen1@example.com", 'password' : HASH } })
	box('email_to_u_id', { "jane.citizen1@example.com" : 1})

	with pytest.raises(ValueError):
		auth_login.auth_login("designedtofail", PASSWORD)

@Virtualized
def test_auth_login_no_such_user():
	box('tokens', [])
	box('users', {"1" : { "u_id": 1, "email": "jane.citizen1@example.com", 'password' : HASH } })
	box('email_to_u_id', {"jane.citizen1@example.com" : 1})

	with pytest.raises(ValueError):
		auth_login.auth_login("bob.johnson@example.com", PASSWORD)

@Virtualized
def test_auth_login_invalid_password():
	box('tokens', [])
	box('users', {"1" : { "u_id": 1, "email": "jane.citizen1@example.com", 'password' : HASH } })
	box('email_to_u_id', {"jane.citizen1@example.com" : 1})

	with pytest.raises(ValueError):
		auth_login.auth_login("jane.citizen1@example.com", "designedtofail")

@Virtualized
def test_auth_login_success():
	box('tokens', [])
	box('users', {"1" : { "u_id": 1, "email": "jane.citizen1@example.com", 'password' : HASH } })
	box('email_to_u_id', {"jane.citizen1@example.com" : 1})

	junk = auth_login.auth_login("jane.citizen1@example.com", PASSWORD)

	tokens = unbox('tokens', [])

	assert junk['token'] in tokens