from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Users
from flask_session import Session
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash

userid = uuid.uuid4()  # to bdo ........... to be return to the setter and getter


def register(data, db):
    firstname = data['fname']
    lastname = data['lname']
    email = data['email']
    userRole = data['role']
    password = data['password']
    phone = data['PhoneNo']
    
    
    # check if user exists
    user = Users.query.filter_by(email=email).first()
    if not user:
        try:
            pas = generate_password_hash(password)
            user = Users(userid=userid, fname=firstname, lname=lastname, role=userRole,
                         email=email, password=pas, PhoneNo=phone) #isadmin=False
            db.session.add(user)
            db.session.commit()

            #.......Send an email...............#
            #sendEmail(user.email, "User created successfully! - Test Email")

            return jsonify({'message': 'doctor registered'}), 200

        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to register a doctor'}), 403
            pass
    return jsonify({'message': 'User already exist!'}), 407
