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

from . import user_profile_sethandle

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.OkPmkNhvSri6ZFlANW46hzcoEgict64PXjVuEYLTwJk"
PASSWORD = "2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b"
USER = { "u_id": 1, "email": "jane.citizen1@example.com",'handle_str': "janecitizen", 'name_first': 'Jane', 'name_last': 'Citizen', 'password' : PASSWORD }

@Virtualized
def test_user_profile_sethandle_invalid_token():
	box('tokens', [TOKEN])
	box('users', {"1" :  USER})
	box('email_to_u_id', { "jane.citizen1@example.com" : 1})
	box('handle_to_u_id', {"janecitizen" : 1})
    
	with pytest.raises(AccessError):
		user_profile_sethandle.user_profile_sethandle("designedtofail", "koolkid")

@Virtualized
def test_user_profile_sethandle_length_issues():
	box('tokens', [TOKEN])
	box('users', {"1" :  USER})
	box('email_to_u_id', { "jane.citizen1@example.com" : 1})
	box('handle_to_u_id', {"janecitizen" : 1})
    
	with pytest.raises(ValueError):
		user_profile_sethandle.user_profile_sethandle(TOKEN, "koolkid" * 50)

@Virtualized
def test_user_profile_sethandle_handle_taken():
	box('tokens', [TOKEN])
	dummy = {"u_id": 1, "email": "jane.citizen1@example.com",'handle_str': "janecitizen", 'name_first': 'Jane', 'name_last': 'Citizen', 'password' : PASSWORD }
	dummy['u_id'] = 2
	dummy['handle_str'] = "koolkid"
	box('users', {"1" :  USER, "2": dummy})
	box('email_to_u_id', { "jane.citizen1@example.com" : 1})
	box('handle_to_u_id', {"janecitizen" : 1, "koolkid" : 2})

	with pytest.raises(ValueError):
		user_profile_sethandle.user_profile_sethandle(TOKEN, "koolkid")

@Virtualized
def test_user_profile_sethandle_success():
	box('tokens', [TOKEN])
	box('users', {"1" :  USER})
	box('email_to_u_id', { "jane.citizen1@example.com" : 1})
	box('handle_to_u_id', {"janecitizen" : 1})
    
	user_profile_sethandle.user_profile_sethandle(TOKEN, "koolkid")

	users = unbox('users', {})
	user = users['1']

	handle_table = unbox('handle_to_u_id', {})
	
	assert "koolkid" in handle_table and "janecitizen" not in handle_table
	assert handle_table["koolkid"] == 1
	assert user['handle_str'] == "koolkid"