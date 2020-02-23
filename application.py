from flask import Flask, request
from flask_cors import CORS
from flask_mail import Mail, Message

from backend.utility import errors

APPLICATION = Flask(__name__)
APPLICATION.debug = True

APPLICATION.config['TRAP_HTTP_EXCEPTIONS'] = True
APPLICATION.register_error_handler(Exception, errors.handler)

APPLICATION.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'lutlyanything@gmail.com',
    MAIL_PASSWORD = 'paxxartoeurfzfbu',
    MAIL_DEFAULT_SENDER = 'lutlyanything@gmail.com'
)

CORS(APPLICATION)
