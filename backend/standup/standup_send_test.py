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

from . import standup_send

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.OkPmkNhvSri6ZFlANW46hzcoEgict64PXjVuEYLTwJk"

@Virtualized
def test_standup_send_success():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, 'handle_str': 'a', "permission_id": 1 }, "2" : { "u_id": 2, 'handle_str': 'b', "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0, 1], 'owner_members': [0]}})
	box('channel_id_to_time_finish', {'1': 3})
	box('channel_id_to_messages', {'1': []})

	standup_send.standup_send(TOKEN, 1, 'test')

	assert unbox('channel_id_to_messages') == {'1': [{'u_id': 1, 'message': 'test'}]}

@Virtualized
def test_standup_send_invalid_token():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, 'handle_str': 'a', "permission_id": 1 }, "2" : { "u_id": 2, 'handle_str': 'b', "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0, 1], 'owner_members': [0]}})
	box('channel_id_to_time_finish', {'1': 3})
	box('channel_id_to_messages', {'1': []})

	with pytest.raises(AccessError):
		standup_send.standup_send("designedtofail", 1, 'test')

@Virtualized
def test_standup_send_invalid_channel():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, 'handle_str': 'a', "permission_id": 1 }, "2" : { "u_id": 2, 'handle_str': 'b', "permission_id": 1 } })

	with pytest.raises(ValueError):
		standup_send.standup_send(TOKEN, 1, 'test')

@Virtualized
def test_standup_send_no_such_standup():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, 'handle_str': 'a', "permission_id": 1 }, "2" : { "u_id": 2, 'handle_str': 'b', "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0, 1], 'owner_members': [0]}})

	with pytest.raises(ValueError):
		standup_send.standup_send(TOKEN, 1, 'test')

@Virtualized
def test_standup_send_not_a_member():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, 'handle_str': 'a', "permission_id": 1 }, "2" : { "u_id": 2, 'handle_str': 'b', "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0], 'owner_members': [0]}})
	box('channel_id_to_time_finish', {'1': 3})
	box('channel_id_to_messages', {'1': []})

	with pytest.raises(AccessError):
		standup_send.standup_send(TOKEN, 1, 'test')

@Virtualized
def test_standup_send_too_long():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, 'handle_str': 'a', "permission_id": 1 }, "2" : { "u_id": 2, 'handle_str': 'b', "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0, 1], 'owner_members': [0]}})
	box('channel_id_to_time_finish', {'1': 3})
	box('channel_id_to_messages', {'1': []})

	with pytest.raises(ValueError):
		standup_send.standup_send(TOKEN, 1, 'test' * 1000)
