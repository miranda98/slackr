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

from . import message_send

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.OkPmkNhvSri6ZFlANW46hzcoEgict64PXjVuEYLTwJk"

@Virtualized
def test_message_send_invalid_token():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }})
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [1], 'owner_members': [1]}})
	box('messages', {})

	with pytest.raises(AccessError):
		message_send.message_send("designedtofail", 1, "Oh Boy")

@Virtualized
def test_message_send_no_such_channel():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }})
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [1], 'owner_members': [1]}})
	box('messages', {})

	with pytest.raises(ValueError):
		message_send.message_send(TOKEN, 5, "Oh Boy")

@Virtualized
def test_message_send_not_a_member():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }})
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [], 'owner_members': []}})
	box('messages', {})

	with pytest.raises(AccessError):
		message_send.message_send(TOKEN, 1, "Oh Boy")

@Virtualized
def test_message_send_too_long():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }})
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [1], 'owner_members': [1]}})
	box('messages', {})

	with pytest.raises(ValueError):
		message_send.message_send(TOKEN, 1, "A" * 1001)

@Virtualized
def test_message_send_success_1():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }})
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [1], 'owner_members': [1]}})
	box('messages', {})

	assert message_send.message_send(TOKEN, 1, "Oh Boy") == {'message_id' : 0}

	messages = unbox('messages')

	assert messages['0'] == {
		'message_id': 0,
		'channel_id': 1,
		'u_id': 1,
		'message': "Oh Boy",
		'time_created': int(time.time()),
		'reacts': {},
		'is_pinned': False
	}

@Virtualized
def test_message_send_success_2():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }})
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [1], 'owner_members': [1]}})
	box('messages', {'0' : {
		'message_id': 0,
		'channel_id': 1,
		'u_id': 1,
		'message': "hello, world!",
		'time_created': int(time.time()),
		'reacts': {},
		'is_pinned': False
	}})

	assert message_send.message_send(TOKEN, 1, "Oh Boy") == {'message_id' : 1}

	messages = unbox('messages')

	assert messages['1'] == {
		'message_id': 1,
		'channel_id': 1,
		'u_id': 1,
		'message': "Oh Boy",
		'time_created': int(time.time()),
		'reacts': {},
		'is_pinned': False
	}
