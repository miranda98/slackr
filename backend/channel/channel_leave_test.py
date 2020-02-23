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

from . import channel_leave

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.OkPmkNhvSri6ZFlANW46hzcoEgict64PXjVuEYLTwJk"

@Virtualized
def test_channel_leave_invalid_token():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }, "2" : { "u_id": 2, "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0, 1], 'owner_members': [0]}})

	with pytest.raises(AccessError):
		channel_leave.channel_leave("designedtofail", 1)

@Virtualized
def test_channel_leave_no_such_channel():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }, "2" : { "u_id": 2, "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0, 1], 'owner_members': [0]}})

	with pytest.raises(ValueError):
		channel_leave.channel_leave(TOKEN, 2);

@Virtualized
def test_channel_leave_success_1():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }, "2" : { "u_id": 2, "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0, 1], 'owner_members': [0]}})

	channel_leave.channel_leave(TOKEN, 1);

	channels = unbox('channels')
	assert 1 not in channels["1"]['all_members'] and 1 not in channels['1']['owner_members']

@Virtualized
def test_channel_leave_success_2():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }, "2" : { "u_id": 2, "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0, 1], 'owner_members': [0, 1]}})

	channel_leave.channel_leave(TOKEN, 1);

	channels = unbox('channels')
	assert 1 not in channels["1"]['all_members'] and 1 not in channels['1']['owner_members']

@Virtualized
def test_channel_leave_success_3():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }, "2" : { "u_id": 2, "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0], 'owner_members': [0]}})

	channel_leave.channel_leave(TOKEN, 1);

	channels = unbox('channels')
	assert 1 not in channels["1"]['all_members'] and 1 not in channels['1']['owner_members']

