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

from . import user_profile_setemail

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.OkPmkNhvSri6ZFlANW46hzcoEgict64PXjVuEYLTwJk"
PASSWORD = "2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b"
USER = { "u_id": 1, "email": "jane.citizen1@example.com",'handle_str': "janecitizen", 'name_first': 'Jane', 'name_last': 'Citizen', 'password' : PASSWORD }

@Virtualized
def test_user_profile_setemail_invalid_token():
	box('tokens', [TOKEN])
	box('users', {"1" :  USER})
	box('email_to_u_id', { "jane.citizen1@example.com" : 1})
	box('handle_to_u_id', {"janecitizen" : 1})
    
	with pytest.raises(AccessError):
		user_profile_setemail.user_profile_setemail("designedtofail", "ohboy@gmail.com")

@Virtualized
def test_user_profile_setemail_invalid_email():
	box('tokens', [TOKEN])
	box('users', {"1" :  USER})
	box('email_to_u_id', { "jane.citizen1@example.com" : 1})
	box('handle_to_u_id', {"janecitizen" : 1})
    
	with pytest.raises(ValueError):
		user_profile_setemail.user_profile_setemail(TOKEN, "designedtofail")

@Virtualized
def test_user_profile_setemail_email_taken():
	box('tokens', [TOKEN])
	dummy = {"u_id": 1, "email": "jane.citizen1@example.com",'handle_str': "janecitizen", 'name_first': 'Jane', 'name_last': 'Citizen', 'password' : PASSWORD }
	dummy['u_id'] = 2
	dummy['email'] = "ohboy@gmail.com"
	box('users', {"1" :  USER, "2": dummy})
	box('email_to_u_id', { "jane.citizen1@example.com" : 1, "ohboy@gmail.com" : 2})
	box('handle_to_u_id', {"janecitizen" : 1, "janecitizen1" : 2})
    
	with pytest.raises(ValueError):
		user_profile_setemail.user_profile_setemail(TOKEN, "ohboy@gmail.com")

@Virtualized
def test_user_profile_setemail_success():
	box('tokens', [TOKEN])
	box('users', {"1" :  USER})
	box('email_to_u_id', { "jane.citizen1@example.com" : 1})
	box('handle_to_u_id', {"janecitizen" : 1})
    
	user_profile_setemail.user_profile_setemail(TOKEN, "ohboy@gmail.com")

	email_table = unbox('email_to_u_id', [])
	users = unbox('users', [])

	assert USER['email'] not in email_table
	assert "ohboy@gmail.com" in email_table
	assert email_table["ohboy@gmail.com"] == 1
	assert users['1']['email'] == "ohboy@gmail.com"