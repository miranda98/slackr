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

from . import auth_register

PASSWORD = "secret"
HASH = hashlib.sha256(PASSWORD.encode()).hexdigest()

@Virtualized
def test_auth_register_invalid_email():
	with pytest.raises(ValueError):
		auth_register.auth_register("designedtofail", "secret", "Jane", "Citizen")

@Virtualized
def test_auth_register_email_used():
	box('users', {"1" : { "u_id": 1, "email": "jane.citizen1@example.com", 'password' : HASH } })
	box('email_to_u_id', { "jane.citizen1@example.com" : 1})
	box('handle_to_u_id', {"janecitizen" : 1})

	with pytest.raises(ValueError):
		auth_register.auth_register("jane.citizen1@example.com", "secret", "Jane", "Citizen")

@Virtualized
def test_auth_register_bad_password():
	with pytest.raises(ValueError):
		auth_register.auth_register("jane.citizen1@example.com", "short", "Jane", "Citizen")

@Virtualized
def test_auth_register_bad_first_name():
	with pytest.raises(ValueError):
		auth_register.auth_register("jane.citizen1@example.com", "secret", "a" * 51, "Citizen")

@Virtualized
def test_auth_register_bad_last_name():
	with pytest.raises(ValueError):
		auth_register.auth_register("jane.citizen1@example.com", "secret", "Jane", "a" * 51)

@Virtualized
def test_auth_register_success_genesis():
	auth_register.auth_register("jane.citizen1@example.com", "secret", "Jane", "Citizen")

	users = unbox('users', {})

	assert users['0'] == {
		'u_id' : 0,
		'email' : "jane.citizen1@example.com",
		'password' : HASH,
		'permission_id' : 1,
		'name_first' : "Jane",
		'name_last' : "Citizen",
		'profile_img_url' : '/user/profiles/photo/default.jpg',
		'handle_str' : "janecitizen"
	}

@Virtualized
def test_auth_register_success_general():
	box('users', {"1" : { "u_id": 1, "permission_id": 1 }})

	auth_register.auth_register("jane.citizen1@example.com", "secret", "Jane", "Citizen")

	users = unbox('users', {})

	assert users['2'] == {
		'u_id' : 2,
		'email' : "jane.citizen1@example.com",
		'password' : HASH,
		'permission_id' : 3,
		'name_first' : "Jane",
		'name_last' : "Citizen",
		'profile_img_url' : '/user/profiles/photo/default.jpg',
		'handle_str' : "janecitizen"
	}

@Virtualized
def test_auth_register_success_long_handle():
	auth_register.auth_register("jane.citizen1@example.com", "secret", "Janeabcdefghijklmnopqrstuvwxyz", "Citizen")

	users = unbox('users', {})

	assert users['0'] == {
		'u_id' : 0,
		'email' : "jane.citizen1@example.com",
		'password' : HASH,
		'permission_id' : 1,
		'name_first' : "Janeabcdefghijklmnopqrstuvwxyz",
		'profile_img_url' : '/user/profiles/photo/default.jpg',
		'name_last' : "Citizen",
		'handle_str' : "janeabcdefghijklmnop"
	}

@Virtualized
def test_auth_register_success_unique_handle():
	box('handle_to_u_id', {"janecitizen" : 1})

	auth_register.auth_register("jane.citizen1@example.com", "secret", "Jane", "Citizen")

	users = unbox('users', {})

	assert users['0'] == {
		'u_id' : 0,
		'email' : "jane.citizen1@example.com",
		'password' : HASH,
		'permission_id' : 1,
		'name_first' : "Jane",
		'name_last' : "Citizen",
		'profile_img_url' : '/user/profiles/photo/default.jpg',
		'handle_str' : "janecitizen1"
	}
