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

from . import channels_list

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.OkPmkNhvSri6ZFlANW46hzcoEgict64PXjVuEYLTwJk"

@Virtualized
def test_channels_list_invalid_token():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 } })

	with pytest.raises(AccessError):
		channels_list.channels_list("designedtofail")

@Virtualized
def test_channels_list_success():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 } })
	box('channels', {
		"1" : {'channel_id': 1, 'name': "1st", 'is_public': True, 'all_members': [0], 'owner_members': [0]},
		"2" : {'channel_id': 2, 'name': "2nd", 'is_public': True, 'all_members': [1], 'owner_members': [0]},
		"3" : {'channel_id': 3, 'name': "3rd", 'is_public': True, 'all_members': [1], 'owner_members': [0, 1]}
	})

	assert channels_list.channels_list(TOKEN) == {'channels': [{ 'channel_id' : 2, 'name' : '2nd' }, { 'channel_id' : 3, 'name' : '3rd' }]}
