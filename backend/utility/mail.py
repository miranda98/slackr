import os
import sys

from flask_mail import Mail, Message

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../')))

from application import APPLICATION

def mail(recipient, subject, message):
    with APPLICATION.app_context():
        MAIL = Mail(APPLICATION)

        msg = Message(subject,
            recipients=[recipient])
        msg.body = message

        MAIL.send(msg)
