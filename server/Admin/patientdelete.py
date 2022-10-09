from jwt import exceptions
from server.models import Users
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash
from sqlalchemy import select, update, delete, values
from ..extensions import db

userid = uuid.uuid4()  # todo ........... to be return to the setter and getter


def removeUser(userid):
    #  userid = data['firstname']
    print(userid)

    try:
        effected_rows = Users.query.filter_by(userid=userid).first()
        print(effected_rows)
        if effected_rows == 0:
            print('user not found')
            return jsonify({'message': 'Failed to delete user'}), 403
        else:
            db.session.commit()
            return jsonify({'message': 'User deleted'}), 200
    except Exception as e:
        
        return jsonify({'message': 'Failed to delete user'}), 403
        pass
