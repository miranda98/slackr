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

from . import channel_messages

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.OkPmkNhvSri6ZFlANW46hzcoEgict64PXjVuEYLTwJk"

@Virtualized
def test_channel_messages_invalid_token():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }, "2" : { "u_id": 2, "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0, 1], 'owner_members': [0, 1]}})
	box('messages', {"1" : {'message_id': 1, 'channel_id': 1, 'message': None, 'u_id' : 1, 'time_created': 1, 'reacts': {}, 'is_pinned': None},
		"2": {'message_id': 2, 'channel_id': 1, 'message': None, 'u_id' : 1, 'time_created': 2, 'reacts': {}, 'is_pinned': None},
		"3": {'message_id': 3, 'channel_id': 1, 'message': None, 'u_id' : 1, 'time_created': 3, 'reacts': {}, 'is_pinned': None}})

	with pytest.raises(AccessError):
		channel_messages.channel_messages("designedtofail", 1, 1)

@Virtualized
def test_channel_messages_no_such_channel():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }, "2" : { "u_id": 2, "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0, 1], 'owner_members': [0, 1]}})
	box('messages', {"1" : {'message_id': 1, 'channel_id': 1, 'message': None, 'u_id' : 1, 'time_created': 1, 'reacts': {}, 'is_pinned': None},
		"2": {'message_id': 2, 'channel_id': 1, 'message': None, 'u_id' : 1, 'time_created': 2, 'reacts': {}, 'is_pinned': None},
		"3": {'message_id': 3, 'channel_id': 1, 'message': None, 'u_id' : 1, 'time_created': 3, 'reacts': {}, 'is_pinned': None}})

	with pytest.raises(ValueError):
		channel_messages.channel_messages(TOKEN, 2, 1);

@Virtualized
def test_channel_messages_not_authenticated():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 3 }, "2" : { "u_id": 2, "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0], 'owner_members': [0]}})
	box('messages', {"1" : {'message_id': 1, 'channel_id': 1, 'message': None, 'u_id' : 1, 'time_created': 1, 'reacts': {}, 'is_pinned': None},
		"2": {'message_id': 2, 'channel_id': 1, 'message': None, 'u_id' : 1, 'time_created': 2, 'reacts': {}, 'is_pinned': None},
		"3": {'message_id': 3, 'channel_id': 1, 'message': None, 'u_id' : 1, 'time_created': 3, 'reacts': {}, 'is_pinned': None}})

	with pytest.raises(AccessError):
		channel_messages.channel_messages(TOKEN, 1, 1);

@Virtualized
def test_channel_messages_funky_start():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }, "2" : { "u_id": 2, "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0, 1], 'owner_members': [0, 1]}})
	box('messages', {"1" : {'message_id': 1, 'channel_id': 1, 'message': None, 'u_id' : 1, 'time_created': 1, 'reacts': {}, 'is_pinned': None},
		"2": {'message_id': 2, 'channel_id': 1, 'message': None, 'u_id' : 1, 'time_created': 2, 'reacts': {}, 'is_pinned': None},
		"3": {'message_id': 3, 'channel_id': 1, 'message': None, 'u_id' : 1, 'time_created': 3, 'reacts': {}, 'is_pinned': None}})

	with pytest.raises(ValueError):
		channel_messages.channel_messages(TOKEN, 1, 500);

@Virtualized
def test_channel_messages_success():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }, "2" : { "u_id": 2, "permission_id": 1 } })
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0, 1], 'owner_members': [0, 1]}})
	box('messages', {"1" : {'message_id': 1, 'channel_id': 1, 'message': None, 'u_id' : 1, 'time_created': 1, 'reacts': {}, 'is_pinned': None},
		"2": {'message_id': 2, 'channel_id': 1, 'message': None, 'u_id' : 1, 'time_created': 2, 'reacts': {}, 'is_pinned': None},
		"3": {'message_id': 3, 'channel_id': 1, 'message': None, 'u_id' : 1, 'time_created': 3, 'reacts': {}, 'is_pinned': None}})

	assert channel_messages.channel_messages(TOKEN, 1, 1) == { 'messages': [{'message_id': 2, 'message': None, 'u_id' : 1, 'time_created': 2, 'reacts':[], 'is_pinned': None},
									{'message_id': 3, 'message': None, 'u_id' : 1, 'time_created': 3, 'reacts': [], 'is_pinned': None}],
								'start' : 1, 'end' : -1}
