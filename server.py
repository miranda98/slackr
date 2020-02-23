import sys

from backend import (admin, auth, channel, channels, message, search, user, users, standup)
from backend.utility.storage import box

from application import APPLICATION

for module in [admin, auth, channel, channels, message, search, user, users, standup]:
    APPLICATION.register_blueprint(module.endpoints)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Usage: python3 server.py backend_port frontend_port")

    backend_port = int(sys.argv[1])

    box('url_base', 'http://localhost:' + str(backend_port))

    APPLICATION.run(port=backend_port)
