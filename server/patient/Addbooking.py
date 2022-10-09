from flask_sqlalchemy import model
from jwt import exceptions
from server.models import Appointment
from flask_session import Session
from flask import jsonify,g
import uuid


appointmentid = uuid.uuid4()  # to bdo ........... to be return to the setter and getter


def addappointment(data, db):
    
    doctorid = data['doctorid']
    bookingdate =data['bookingdate']
    
    
    
    
    # check if user exists
    appointment = Appointment.query.filter_by(patientid=g.userid).first()
    if not appointment:
        try:
            appointment = Appointment(patientid=g.userid,doctorid=doctorid,appointmentid=appointmentid, bookingdate=bookingdate, status="pending") 
            db.session.add(appointment)
            db.session.commit()

            
            #.......Send an email...............#
            #sendEmail(user.email, "User created successfully! - Test Email")

            return jsonify({'message': 'appointment added'}), 200

        except Exception as e:
            print(e)
            return jsonify({'message': 'Failed to add appointment'}), 403
            pass
    return jsonify({'message': 'Appointment already exist!'}), 407
