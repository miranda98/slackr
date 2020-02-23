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

from . import standup_start

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.OkPmkNhvSri6ZFlANW46hzcoEgict64PXjVuEYLTwJk"

@Virtualized
def test_standup_start_success():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, 'handle_str': 'a', "permission_id": 1 }, "2" : { "u_id": 2, 'handle_str': 'b', "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0, 1], 'owner_members': [0]}})

	thenish = int(time.time()) + 3

	assert standup_start.standup_start(TOKEN, 1, 3) == {'time_finish': thenish }

	channel_id_to_time_finish = unbox('channel_id_to_time_finish', {})
	channel_id_to_messages = unbox('channel_id_to_messages', {})

	assert channel_id_to_time_finish['1'] == thenish
	assert channel_id_to_messages['1'] == []

	box('channel_id_to_messages', {'1': [{'u_id': 1, 'message': 'test'}]})

	time.sleep(5)

	messages = unbox('messages', [])

	channel_id_to_time_finish = unbox('channel_id_to_time_finish', {})
	channel_id_to_messages = unbox('channel_id_to_messages', {})

	assert len(messages) == 1
	assert '1' not in channel_id_to_time_finish
	assert '1' not in channel_id_to_messages

@Virtualized
def test_standup_start_invalid_token():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, 'handle_str': 'a', "permission_id": 1 }, "2" : { "u_id": 2, 'handle_str': 'b', "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0, 1], 'owner_members': [0]}})

	with pytest.raises(AccessError):
		standup_start.standup_start("designedtofail", 1, 3)

@Virtualized
def test_standup_start_no_such_channel():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, 'handle_str': 'a', "permission_id": 1 }, "2" : { "u_id": 2, 'handle_str': 'b', "permission_id": 1 } })

	with pytest.raises(ValueError):
		standup_start.standup_start(TOKEN, 1, 3)

@Virtualized
def test_standup_start_already_standup():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, 'handle_str': 'a', "permission_id": 1 }, "2" : { "u_id": 2, 'handle_str': 'b', "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0, 1], 'owner_members': [0]}})
	box('channel_id_to_time_finish', {'1': None})

	with pytest.raises(ValueError):
		standup_start.standup_start(TOKEN, 1, 3)
