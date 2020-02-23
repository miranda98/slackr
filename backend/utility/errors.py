from json import dumps

class AccessError(Exception):

    def __init__(self, message):
        self.name = "Unauthorized"
        self.message = message
        self.code = 401


class ValueError(Exception):

    def __init__(self, message):
        self.name = "Bad Request"
        self.message = message
        self.code = 400


def handler(error):
    code = 500 if not hasattr(error, 'code') else error.code
    return dumps({
        'name': error.__class__.__name__,
        'code': code,
        'message': 'Server Error' if not hasattr(error, 'message') else error.message,
        'garbage': str(error)
    }), code
