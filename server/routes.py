from flask import Blueprint, request, jsonify, g
from .extensions import db
from .models import Users,Appointment
from .auth.login import login
from .doctorprofile.profile import createprofile
from .patient.finddoctors import doctors
from .auth.register import register
from .patient.Addbooking import addappointment
from .doctorprofile.viewappointment import getappointment
from .Admin.patientdelete import removeUser
from .Admin.users import users
from .profile.userRole import getUserbyrole
from .helper import token_required_user, token_required_admin,token_required_doctor
from .profile.userProfile import profile
from flask_cors import CORS, cross_origin



main = Blueprint('main', __name__)
CORS(main, support_credentials=True)


# ---------- Authentication routes ----------

@main.route('/register', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def Userreg():
    if(request.method == 'POST'):
        data = request.json
        return register(data, db)
        
    else:
        pass
    


@main.route('/login', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
def Userlogin():
    if(request.method == 'POST'):
        return login(request, Users)
    else:
        pass


@main.route('/resetPassword')
def resetPassword():
    return 'reset codes sent'

# ---------- Admin actions ---------------------------


@main.route('/admin/create-user',  methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def createUser():
    data = request.json
    if(request.method == 'POST'):
        return registerUser(data, db)
    else:
        pass

#----------Doctorprofile routes------------------------
@main.route('/profile', methods=['POST', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_doctor
def patientreg():
    data = request.json
    return createprofile(data, db)

#--------Admin_actions----------------------------------

@main.route('/Admin/register', methods=['POST',''])
@cross_origin(supports_credentials=True)
@token_required_admin
def Docreg():
    data = request.json
    return register(data, db)


@main.route('/Admin/patientdelete/<email>', methods=['DELETE'])
@cross_origin(supports_credentials=True)
@token_required_admin
def remove(email):
    if(request.method == 'DELETE'):
        return removeUser(email)
    else:
        pass
    

#-----------get user-----------------
@main.route('/Admin/users',  methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def getusers():
    if(request.method == 'GET'):
        return users(Users)
    else:
        pass

#----------patient finds doctor-------------
@main.route('/patient/finddoctors',  methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_user
def getdoctors():
    if(request.method == 'GET'):
        return doctors(Users)
    else:
        pass

#----------patient create appointment----------
@main.route('/patient/Addbooking', methods=['POST'])
@cross_origin(supports_credentials=True)
@token_required_user
def bookappointment():
    data = request.json
    return addappointment(data, db)

#----------doctor views appointment-------------
@main.route('/doctorprofile/viewappointment',  methods=['GET', 'OPTIONS'])
@cross_origin(supports_credentials=True)
@token_required_doctor
def viewappointment():
    if(request.method == 'GET'):
        return getappointment(Appointment)
    else:
        pass