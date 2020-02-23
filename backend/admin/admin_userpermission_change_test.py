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

from . import admin_userpermission_change

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.OkPmkNhvSri6ZFlANW46hzcoEgict64PXjVuEYLTwJk"

@Virtualized
def test_admin_userpermission_change_invalid_token():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, 'permission_id': 1 }, "2" : { "u_id": 2, 'permission_id': 3 } })
	
	with pytest.raises(AccessError):
		admin_userpermission_change.admin_userpermission_change("designedtofail", 2, 1)

@Virtualized
def test_admin_userpermission_change_invalid_permission():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, 'permission_id': 3 }, "2" : { "u_id": 2, 'permission_id': 3 } })
	
	with pytest.raises(AccessError):
		admin_userpermission_change.admin_userpermission_change(TOKEN, 2, 1)

@Virtualized
def test_admin_userpermission_change_no_such_user():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, 'permission_id': 1 }, "2" : { "u_id": 2, 'permission_id': 3 } })
	
	with pytest.raises(ValueError):
		admin_userpermission_change.admin_userpermission_change(TOKEN, 5, 1)

@Virtualized
def test_admin_userpermission_change_admin_to_owner():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, 'permission_id': 2 }, "2" : { "u_id": 2, 'permission_id': 1 } })
	
	with pytest.raises(AccessError):
		admin_userpermission_change.admin_userpermission_change(TOKEN, 2, 3)

@Virtualized
def test_admin_userpermission_invalid_permission_id():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, 'permission_id': 1 }, "2" : { "u_id": 2, 'permission_id': 3 } })
	
	with pytest.raises(ValueError):
		admin_userpermission_change.admin_userpermission_change(TOKEN, 2, 5)

@Virtualized
def test_admin_userpermission_change_success():
	box('tokens', [TOKEN])
	box('users', {"1" : { "u_id": 1, 'permission_id': 1 }, "2" : { "u_id": 2, 'permission_id': 3 } })
	
	admin_userpermission_change.admin_userpermission_change(TOKEN, 2, 1)

	users = unbox('users', [])
	user = users['2']

	assert user['permission_id'] == 1