import os
import jwt

SECRET = None

FILE_NAME = os.path.join(os.path.dirname(__file__), 'secret.txt')

with open(FILE_NAME, 'r') as f:
	SECRET = f.read()

assert SECRET != None

def encode(payload):
	return str(jwt.encode(payload, SECRET, algorithm='HS256').decode('utf-8'))

def decode(token):
	return jwt.decode(token, SECRET, algorithms=['HS256'])
