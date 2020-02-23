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
@Identified
def admin_userpermission_change(token, u_id, permission_id):
	users = unbox('users', {})

	auth = users[str(decode(token)['u_id'])]
	user = users[str(u_id)]

	if auth['permission_id'] == 3:
		raise AccessError("Unauthorised")

	if permission_id not in [1, 2, 3]:
		raise ValueError(f"Invalid ID: permission_id - {permission_id}")

	if  auth['permission_id'] > user['permission_id']:
		raise AccessError("Unauthorised")

	user['permission_id'] = permission_id

	users[str(u_id)] = user

	box('users', users)

	return {}
