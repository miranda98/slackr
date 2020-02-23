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
def search(token, query_str):
	users = unbox('users', {})
	channels = unbox('channels', {})
	messages = unbox('messages', {})

	auth = users[str(decode(token)['u_id'])]
	their_channels = [int(id) for id in channels if auth['u_id'] in channels[id]['all_members']]
    
    
    # A dictionary {'messages' : [ list of messages ]}
    # Line 38 contains conditional expression to check message satisfies search criteria
	return { 'messages' : [{'message_id' : m['message_id'],
		'u_id': m['u_id'],
		'message': m['message'],
		'time_created': m['time_created'],
		'reacts' : [{ 'react_id': r['react_id'],
			'u_ids': r['u_ids'],
			'is_this_user_reacted': (auth['u_id'] in r['u_ids'])
			} for r in m['reacts'].values()],
		'is_pinned': m['is_pinned']
		} for m in messages.values() if m['channel_id'] in their_channels and query_str in m['message']]}
