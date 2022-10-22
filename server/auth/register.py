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
    password = data['password']
    PhoneNo = data['phoneNo']
    
    
    # check if user exists
    user = Users.query.filter_by(email=email).first()
    if not user:
        try:
            pas = generate_password_hash(password)
            user = Users(userid=userid, fname=firstname, lname=lastname, role='patient',
                         email=email, password=pas, PhoneNo=PhoneNo) 
            db.session.add(user)
            db.session.commit()

            #.......Send an email...............#
            #sendEmail(user.email, "User created successfully! - Test Email")

            return jsonify({'message': 'user registered'}), 200

        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to register'}), 403
            pass
    return jsonify({'message': 'User already exist!'}), 407
