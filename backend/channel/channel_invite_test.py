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

from . import channel_invite

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.OkPmkNhvSri6ZFlANW46hzcoEgict64PXjVuEYLTwJk"

@Virtualized
def test_channel_invite_invalid_token():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }, "2" : { "u_id": 2, "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0, 1], 'owner_members': [0, 1]}})

	with pytest.raises(AccessError):
		channel_invite.channel_invite("designedtofail", 1, 2)

@Virtualized
def test_channel_invite_no_such_channel():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }, "2" : { "u_id": 2, "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0, 1], 'owner_members': [0, 1]}})

	with pytest.raises(ValueError):
		channel_invite.channel_invite(TOKEN, 2, 2)



@Virtualized
def test_channel_invite_not_authenticated():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 3 }, "2" : { "u_id": 2, "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0], 'owner_members': [0]}})

	with pytest.raises(AccessError):
		channel_invite.channel_invite(TOKEN, 1, 2)

@Virtualized
def test_channel_invite_no_such_user():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }, "2" : { "u_id": 2, "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0, 1], 'owner_members': [0, 1]}})

	with pytest.raises(ValueError):
		channel_invite.channel_invite(TOKEN, 1, 3)

@Virtualized
def test_channel_invite_already_member():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }, "2" : { "u_id": 2, "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0, 1, 2], 'owner_members': [0, 1, 2]}})

	with pytest.raises(ValueError):
		channel_invite.channel_invite(TOKEN, 1, 2)

@Virtualized
def test_channel_invite_success():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }, "2" : { "u_id": 2, "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0, 1], 'owner_members': [0, 1]}})

	channel_invite.channel_invite(TOKEN, 1, 2)

	channels = unbox('channels')
	assert 2 in channels["1"]['all_members']
