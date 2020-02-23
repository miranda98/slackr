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

from . import channels_listall, channels_create

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.OkPmkNhvSri6ZFlANW46hzcoEgict64PXjVuEYLTwJk"

@Virtualized
def test_channels_listall_invalid_token():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 } })

	with pytest.raises(AccessError):
		channels_listall.channels_listall("designedtofail")

@Virtualized
def test_channels_listall_success():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, "permission_id": 1 } })

	channels_create.channels_create(TOKEN, "A", True)
	channels_create.channels_create(TOKEN, "B", False)
	channels_create.channels_create(TOKEN, "C", True)

	assert channels_listall.channels_listall(TOKEN) == {'channels': [{ 'channel_id' : 0, 'name' : 'A' }, { 'channel_id' : 1, 'name' : 'B' }, { 'channel_id' : 2, 'name' : 'C' }]}
