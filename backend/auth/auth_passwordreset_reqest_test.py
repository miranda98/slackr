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

from . import auth_passwordreset_request

PASSWORD = "secret"
HASH = hashlib.sha256(PASSWORD.encode()).hexdigest()
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.OkPmkNhvSri6ZFlANW46hzcoEgict64PXjVuEYLTwJk"

@Virtualized
def test_auth_passwordreset_request_unknown_email():
    box('users', {"1" : { "u_id": 1, "email": "jane.citizen1@example.com", 'password' : HASH } })
    box('email_to_u_id', { "jane.citizen1@example.com" : 1})
    box('handle_to_u_id', {"janecitizen" : 1})

    with pytest.raises(ValueError):
        auth_passwordreset_request.auth_passwordreset_request("designedtofail")

@Virtualized
def test_auth_passwordreset_request_success():
    box('users', {"1" : { "u_id": 1, "email": 'lutlyanything@gmail.com', 'password' : HASH } })
    box('email_to_u_id', { 'lutlyanything@gmail.com' : 1})
    box('handle_to_u_id', {"janecitizen" : 1})

    auth_passwordreset_request.auth_passwordreset_request('lutlyanything@gmail.com')

    reset_code_to_u_id = unbox('reset_code_to_u_id', {})

    assert reset_code_to_u_id and 1 in reset_code_to_u_id.values()
