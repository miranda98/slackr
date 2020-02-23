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

from . import channel_details

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.OkPmkNhvSri6ZFlANW46hzcoEgict64PXjVuEYLTwJk"

@Virtualized
def test_channel_details_invalid_token():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }, "2" : { "u_id": 2, "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0, 1, 2], 'owner_members': [0, 1, 2]}})

	with pytest.raises(AccessError):
		channel_details.channel_details("designedtofail", 1)

@Virtualized
def test_channel_details_no_such_channel():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }, "2" : { "u_id": 2, "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0, 1, 2], 'owner_members': [0, 1, 2]}})

	with pytest.raises(ValueError):
		channel_details.channel_details(TOKEN, 2)

@Virtualized
def test_channel_details_not_authenticated():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 3 }, "2" : { "u_id": 2, "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0, 2], 'owner_members': [0, 2]}})

	with pytest.raises(AccessError):
		channel_details.channel_details(TOKEN, 1)

@Virtualized
def test_channel_details_success():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "name_first": 'a', "name_last": 'b', "profile_img_url": 'c', "permission_id": 1 }, 
		"2" : { "u_id": 2, "name_first": 'a', "name_last": 'b', "profile_img_url": 'c', "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [1, 2], 'owner_members': [1, 2]}})

	assert channel_details.channel_details(TOKEN, 1) == {'name' : '1st', 
		'owner_members': [{"u_id": 1, "name_first": 'a', "name_last": 'b', "profile_img_url": 'c'}, {"u_id": 2, "name_first": 'a', "name_last": 'b', "profile_img_url": 'c'}], 
		'all_members': [{"u_id": 1, "name_first": 'a', "name_last": 'b', "profile_img_url": 'c'}, {"u_id": 2, "name_first": 'a', "name_last": 'b', "profile_img_url": 'c'}]}
	
