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

from PIL import Image
import urllib

@Secured
def user_profiles_uploadphoto(token, img_url, x_start, y_start, x_end, y_end):
    if img_url[-4:] != '.jpg' and img_url[-5:] != '.jpeg':
        raise ValueError(f"Invalid url: '{img_url}'")

    identifier = str(uuid.uuid4())

    PROFILE_IMG_URL = unbox('url_base', '') + '/user/profiles/photo/' + identifier + '.jpg'
    FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../utility/storage/' + identifier + '.jpg')

    try:
        urllib.request.urlretrieve(img_url, FILE)
    except Exception:
        raise ValueError(f"Cannot retrieve image: '{img_url}'")

    try:
        img = Image.open(FILE)
        cropped = img.crop((x_start, y_start, x_end, y_end))
        cropped.save(FILE)
    except Exception:
        os.remove(FILE)
        raise ValueError("Cannot crop image")

    users = unbox('users', [])
    users[str(decode(token)['u_id'])]['profile_img_url'] = PROFILE_IMG_URL
    box('users', users)

    return {}
