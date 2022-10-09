from flask import jsonify
import json

from ..helper import profile_serializer,users_serializer
def doctors(Users):
    pages_perpage = 100
    page = 1
    profile = Users.query.filter_by(role='doctor').order_by(
        Users.created.desc())
    if profile:
       data = [*map(users_serializer, profile)]
       return {'data': data}
    return jsonify({'message' : 'Users not found'}),403
