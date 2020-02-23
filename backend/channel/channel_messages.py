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
def channel_messages(token, channel_id, start):
	users = unbox('users', {})
	channels = unbox('channels', {})
	messages = unbox('messages', {})

	auth = users[str(decode(token)['u_id'])]

	channel = channels[str(channel_id)]

	if auth['u_id'] not in channel['all_members']:
		raise AccessError("Unauthorised")

	messages = [{'message_id' : m['message_id'],
		'u_id' : m['u_id'],
	  	'time_created' : m['time_created'],
	  	'reacts' : [{
			'react_id': r['react_id'],
			'u_ids': r['u_ids'],
			'is_this_user_reacted': (auth['u_id'] in r['u_ids'])
		} for r in m['reacts'].values()],
	  	'is_pinned': m['is_pinned'],
	  	'message' : m['message']
	} for m in sorted([m for m in messages.values() if m['channel_id'] == channel_id], key = lambda k: k['time_created'])]

	count = len(messages)

	if start > count:
		raise ValueError("Requesting out of range messages")

	end = -1 if count - start < 50 else start + 50

	return { 'messages': messages[start:] if end == -1 else messages[start:end - 1], 'start': start, 'end': end }
