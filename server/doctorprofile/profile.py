from server.models import Patientprofile
from flask_session import Session
from flask import jsonify
#import uuid
#from werkzeug.security import generate_password_hash




def createprofile(data, db):
    fname = data['fname']
    lname = data['lname']
    residence=data['residence']
    contacts = data['contacts']
    description = data['history']
    
    
    # check if patient exists
    patient = Patientprofile.query.filter_by(contacts=contacts).first()
    if not patient:
        try:
            patient = Patientprofile( fname=fname, lname=lname, residence=residence,
                         contacts=contacts, history=description) 
            db.session.add(patient)
            db.session.commit()
            return jsonify({'message': 'patient profile added'}), 200

        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to add a patient'}), 403
            pass
    return jsonify({'message': 'patient already exist!'}), 407
