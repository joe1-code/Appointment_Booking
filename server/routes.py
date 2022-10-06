from flask import Blueprint, request, jsonify
from .extensions import db
from .models import Users
from .auth.login import login
from .auth.register import register
from .profile.team import users
from .profile.userRole import getUserbyrole
from .helper import token_required_user, token_required_admin
from .profile.userProfile import profile
from flask_cors import CORS, cross_origin

main = Blueprint('main', __name__)
CORS(main, support_credentials=True)


# ---------- Authentication routes ----------

@main.route('/register', methods=['POST'])
def Userreg():
    data = request.json
    return register(data, db)


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
        return 'registerUser(data, db)'
    else:
        pass
