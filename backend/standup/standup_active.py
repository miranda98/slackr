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
def standup_active(token, channel_id):
    channel_id_to_time_finish = unbox('channel_id_to_time_finish', {})

    is_active = (str(channel_id) in channel_id_to_time_finish)
    time_finish = None if not is_active else channel_id_to_time_finish[str(channel_id)]

    return { 'is_active': is_active, 'time_finish': time_finish }
