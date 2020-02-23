from flask import Blueprint, request
from json import dumps

from . import (search)

endpoints = Blueprint('search', __name__)

@endpoints.route("/search", methods=['GET'])
def endpoint_search():
	token = str(request.args.get('token'))
	query_str = str(request.args.get('query_str'))

	return dumps(search.search(token, query_str))
