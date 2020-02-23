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

from . import channels_create

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.OkPmkNhvSri6ZFlANW46hzcoEgict64PXjVuEYLTwJk"

@Virtualized
def test_channels_create_invalid_token():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 } })

	with pytest.raises(AccessError):
		channels_create.channels_create("designedtofail", "Example Channel", True)

@Virtualized
def test_channels_create_unauthorised_user():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 3 } })

	with pytest.raises(AccessError):
		channels_create.channels_create(TOKEN, "Example Channel", True)

@Virtualized
def test_channels_create_name_too_long():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 } })

	with pytest.raises(ValueError):
		channels_create.channels_create(TOKEN, "Example Channel <----------", True)

@Virtualized
def test_channels_create_success():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 } })

	channels_create.channels_create(TOKEN, "Example Channel", True)

	channels = unbox('channels')
	assert channels["0"] == {'channel_id': 0, 'name': "Example Channel", 'is_public': True, 'all_members': [1], 'owner_members': [1]}
