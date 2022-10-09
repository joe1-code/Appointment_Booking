from flask import jsonify
import json

from ..helper import profile_serializer,users_serializer
def users(Users):
    pages_perpage = 100
    page = 1
    profile = Users.query.filter_by().order_by(
        Users.created.desc())
    if profile:
       data = [*map(users_serializer, profile)]
       return {'data': data}
    return jsonify({'message' : 'Users not found'}),403
