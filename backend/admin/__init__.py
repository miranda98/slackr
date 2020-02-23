from flask import Blueprint, request
from json import dumps

from . import (admin_userpermission_change)

endpoints = Blueprint('admin', __name__)

@endpoints.route("/admin/userpermission/change", methods=['POST'])
def endpoint_admin_userpermission_change():
	token = str(request.form.get('token'))
	u_id = int(request.form.get('u_id'))
	permission_id = int(request.form.get('permission_id'))

	return dumps(admin_userpermission_change.admin_userpermission_change(token, u_id, permission_id))
