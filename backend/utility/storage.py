import os
import json

FILE_NAME = os.path.join(os.path.dirname(__file__), 'datastore.json')

""" Box/Unbox """

def box(key, value):
    box = unpack()

    box[key] = value
    pack(box)

def unbox(key, value=None):
    box = unpack()

    return value if key not in box else box[key]

""" Pack/Unpack """

def pack(data):
    with open(FILE_NAME, 'w') as file:
        json.dump(data, file)

def unpack():
    if not os.path.exists(FILE_NAME):
        return {}

    with open(FILE_NAME, 'r') as file:
        return json.load(file)
