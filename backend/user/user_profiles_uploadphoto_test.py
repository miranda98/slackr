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

from . import user_profiles_uploadphoto

TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1X2lkIjoxfQ.OkPmkNhvSri6ZFlANW46hzcoEgict64PXjVuEYLTwJk"
IMG_URL = 'https://getlol.info/wp-content/uploads/2012/05/am-enjoying-that.jpeg'
PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../utility/storage/')

@Virtualized
def test_user_profiles_uploadphoto_success():
    box('tokens', [TOKEN])
    box('users', {"1" : { "u_id": 1 }})

    pre = len(os.listdir(PATH))

    user_profiles_uploadphoto.user_profiles_uploadphoto(TOKEN, IMG_URL, 0, 0, 580, 390)

    post = len(os.listdir(PATH))

    users = unbox('users')
    assert 'profile_img_url' in users['1']
    assert post - pre == 1

@Virtualized
def test_user_profiles_uploadphoto_invalid_token():
    box('tokens', [TOKEN])
    box('users', {"1" : { "u_id": 1 }})

    with pytest.raises(AccessError):
        user_profiles_uploadphoto.user_profiles_uploadphoto("designedtofail", IMG_URL, 0, 0, 580, 390)

@Virtualized
def test_user_profiles_uploadphoto_invalid_type():
    box('tokens', [TOKEN])
    box('users', {"1" : { "u_id": 1 }})

    with pytest.raises(ValueError):
        user_profiles_uploadphoto.user_profiles_uploadphoto(TOKEN, "designedtofail", 0, 0, 580, 390)

@Virtualized
def test_user_profiles_uploadphoto_bad_url():
    box('tokens', [TOKEN])
    box('users', {"1" : { "u_id": 1 }})

    with pytest.raises(ValueError):
        user_profiles_uploadphoto.user_profiles_uploadphoto(TOKEN, "designedtofail.jpeg", 0, 0, 580, 390)

@Virtualized
def test_user_profiles_uploadphoto_bad_crop():
    box('tokens', [TOKEN])
    box('users', {"1" : { "u_id": 1 }})

    with pytest.raises(ValueError):
        user_profiles_uploadphoto.user_profiles_uploadphoto(TOKEN, IMG_URL, 2000, 1500, 580, 390)
