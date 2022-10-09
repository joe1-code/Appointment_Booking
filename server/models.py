from enum import unique
from sqlalchemy import null
from .extensions import db
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
#import uuid


#userid = uuid.uuid4()


class Users(db.Model):

    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(200), nullable=False, unique=True)
    fname = db.Column(db.String(200), nullable=False)
    lname = db.Column(db.String(200), nullable=False)
    role=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(200),nullable=False,unique=True)
    password=db.Column(db.String(200),nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow)
    PhoneNo=db.Column(db.Integer,nullable=False,unique=True)

#create table for a patient
class Patientprofile(db.Model):

    __tablename__= 'Patientprofile'

    id =db.Column(db.Integer, primary_key=True)
    fname =db.Column(db.String(200), nullable=False)
    lname =db.Column(db.String(200), nullable=False)
    residence =db.Column(db.String(200), nullable=False)
    contacts =db.Column(db.String(200), nullable=False, unique=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow)
    history =db.Column(db.String(200), nullable=False)

#Table for appointment creation
class Appointment(db.Model):

    __tablename__ = 'Appointment'

    id = db.Column(db.Integer, primary_key=True)
    patientid = db.Column(db.String(200), nullable=False, unique=True)
    doctorid = db.Column(db.String(200), nullable=False, unique=True)
    appointmentid = db.Column(db.String(200), nullable=False, unique=True)
    bookingdate = db.Column(db.String(200), nullable=False)
    status =db.Column(db.String(200),nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime, default=datetime.utcnow)
    
    
    