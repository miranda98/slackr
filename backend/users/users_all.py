""" Module Based Imports """
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))

from utility.storage import box, unbox
from utility.errors import ValueError, AccessError
from utility.security import encode, decode
from utility.wrappers import Virtualized, Secured, Identified

""" Other Imports """

import re, hashlib, time, uuid

""" Implementation """

@Secured
def users_all(token):
    return { 'users': [{
        'u_id': u['u_id'],
        'email': u['email'],
        'name_first': u['name_first'],
        'name_last': u['name_last'],
        'handle_str': u['handle_str'],
        'profile_img_url': u['profile_img_url']
    } for u in unbox('users', {}).values()]}
