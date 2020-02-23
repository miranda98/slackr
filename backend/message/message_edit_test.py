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

from . import message_edit

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.OkPmkNhvSri6ZFlANW46hzcoEgict64PXjVuEYLTwJk"

@Virtualized
def test_message_edit_invalid_token():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }})
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [1], 'owner_members': [1]}})
	box('messages', {'0' : {
		'message_id': 0,
		'channel_id': 1,
		'u_id': 1,
		'message': "hello, world!",
		'time_created': time.asctime(),
		'reacts': {},
		'is_pinned': False 
	}})
	
	with pytest.raises(AccessError):
		message_edit.message_edit("designedtofail", 0, "different")

@Virtualized
def test_message_edit_no_such_message():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }})
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [1], 'owner_members': [1]}})
	box('messages', {})
	
	with pytest.raises(ValueError):
		message_edit.message_edit(TOKEN, 0, "different")

@Virtualized
def test_message_edit_not_authorized():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 3 }})
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [], 'owner_members': []}})
	box('messages', {'0' : {
		'message_id': 0,
		'channel_id': 1,
		'u_id': 3,
		'message': "hello, world!",
		'time_created': time.asctime(),
		'reacts': {},
		'is_pinned': False 
	}})
	
	with pytest.raises(AccessError):
		message_edit.message_edit(TOKEN, 0, "different")

@Virtualized
def test_message_edit_success():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }})
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [1], 'owner_members': [1]}})
	box('messages', {'0' : {
		'message_id': 0,
		'channel_id': 1,
		'u_id': 1,
		'message': "hello, world!",
		'time_created': time.asctime(),
		'reacts': {},
		'is_pinned': False 
	}})
	
	message_edit.message_edit(TOKEN, 0, "different")

	messages = unbox('messages')

	assert messages['0']['message'] == "different"

@Virtualized
def test_message_edit_success_remove():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }})
	box('channels', {"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [1], 'owner_members': [1]}})
	box('messages', {'0' : {
		'message_id': 0,
		'channel_id': 1,
		'u_id': 1,
		'message': "hello, world!",
		'time_created': time.asctime(),
		'reacts': {},
		'is_pinned': False 
	}})
	
	message_edit.message_edit(TOKEN, 0, "")

	messages = unbox('messages')

	assert not messages
