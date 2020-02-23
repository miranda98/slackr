from functools import wraps
from inspect import signature

from .storage import pack, unpack, box, unbox
from .errors import ValueError, AccessError

def Virtualized(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        data = unpack()
        pack({})

        function(*args, **kwargs)

        pack(data)
    return wrapper

def Secured(function):
    sig = signature(function)

    @wraps(function)
    def wrapper(*args, **kwargs):
        bind = sig.bind(*args, **kwargs)
        bind.apply_defaults()

        zargs = dict(bind.arguments)

        assert 'token' in zargs

        token = zargs['token']

        if token not in unbox('tokens', []):
            raise AccessError(f"Invalid Token: '{token}'")
        else:
            return function(*args, **kwargs)
    return wrapper

def Identified(function):
    sig = signature(function)

    @wraps(function)
    def wrapper(*args, **kwargs):
        bind = sig.bind(*args, **kwargs)
        bind.apply_defaults()

        zargs = dict(bind.arguments)

        switcher = {
            'u_id': 'users',
            'message_id': 'messages',
            'channel_id': 'channels',
        }

        assert [z for z in zargs if z in switcher]

        for zarg in zargs:
            if zarg in switcher:
                id = str(zargs[zarg])
                if id not in unbox(switcher[zarg], {}):
                    raise ValueError(f"Invalid ID: {zarg} - {id}")
        return function(*args, **kwargs)
    return wrapper
