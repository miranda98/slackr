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

from . import users_all

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.OkPmkNhvSri6ZFlANW46hzcoEgict64PXjVuEYLTwJk"
PASSWORD = "2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b"
USER = { "u_id": 1, "email": "jane.citizen1@example.com",'handle_str': "janecitizen", 'name_first': 'Jane', 'name_last': 'Citizen', 'password' : PASSWORD, 'profile_img_url': 'www.com' }

@Virtualized
def test_users_all_success():
	box('tokens', [TOKEN])
	box('users', {"1" :  USER})
	box('email_to_u_id', { "jane.citizen1@example.com" : 1})
	box('handle_to_u_id', {"janecitizen" : 1})
    
	assert users_all.users_all(TOKEN) == {'users': 
                                            [{'u_id': USER['u_id'],
                                            'email': USER['email'], 
                                           'name_first': USER['name_first'],
                                           'name_last': USER['name_last'], 
                                           'handle_str': USER['handle_str'],
                                           'profile_img_url': USER['profile_img_url']}]}

@Virtualized
def test_users_all_invalid_token():
	box('tokens', [TOKEN])
	box('users', {"1" :  USER})
	box('email_to_u_id', { "jane.citizen1@example.com" : 1})
	box('handle_to_u_id', {"janecitizen" : 1})
    
	with pytest.raises(AccessError):
		users_all.users_all("designedtofail")