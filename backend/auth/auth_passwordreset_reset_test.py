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

from . import auth_passwordreset_reset

PASSWORD = "secret"
HASH = hashlib.sha256(PASSWORD.encode()).hexdigest()

NEW_PASSWORD = "password"
NEW_HASH = hashlib.sha256(NEW_PASSWORD.encode()).hexdigest()

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.OkPmkNhvSri6ZFlANW46hzcoEgict64PXjVuEYLTwJk"

@Virtualized
def test_auth_passwordreset_reset_unknown_code():
	box('users', {"1" : { "u_id": 1, "email": "jane.citizen1@example.com", 'password' : HASH } })
	box('email_to_u_id', { "jane.citizen1@example.com" : 1})
	box('handle_to_u_id', {"janecitizen" : 1})
	box('reset_code_to_u_id', {"abcde" : 1})

	with pytest.raises(ValueError):
		auth_passwordreset_reset.auth_passwordreset_reset("designedtofail", NEW_PASSWORD)

@Virtualized
def test_auth_passwordreset_reset_invalid_password():
	box('users', {"1" : { "u_id": 1, "email": "jane.citizen1@example.com", 'password' : HASH } })
	box('email_to_u_id', { "jane.citizen1@example.com" : 1})
	box('handle_to_u_id', {"janecitizen" : 1})
	box('reset_code_to_u_id', {"abcde" : 1})

	with pytest.raises(ValueError):
		auth_passwordreset_reset.auth_passwordreset_reset("abcde", "woops")

@Virtualized
def test_auth_passwordreset_reset_success():
	box('users', {"1" : { "u_id": 1, "email": "jane.citizen1@example.com", 'password' : HASH } })
	box('email_to_u_id', { "jane.citizen1@example.com" : 1})
	box('handle_to_u_id', {"janecitizen" : 1})
	box('reset_code_to_u_id', {"abcde" : 1})

	auth_passwordreset_reset.auth_passwordreset_reset("abcde", NEW_PASSWORD)

	reset_code_to_u_id = unbox('reset_code_to_u_id', {})
	user = unbox('users')['1']

	assert not reset_code_to_u_id and user['password'] == NEW_HASH