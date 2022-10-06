from flask import jsonify, g
from ..helper import profile_serializer
from ..models import Users


def profile(userId, Users):
    profile = Users.query.filter_by(userid=userId).first()
    employes = Users.query.filter_by()

    if profile:
        data = {'username': profile.fname, 'fname': profile.fname, 'lname': profile.lname, 'userRole': profile.role,
                'phone': profile.phone, 'email': profile.email, 'branchId': profile.branchId, 'dashData': {'branches': branch.count(), 'vehicles': vehicle.count(), 'customers': customer.count(), 'employes': employes.count(), 'transporters': transporter.count()}}
        return jsonify(data), 200
    return jsonify({'message': 'User not found'}), 403
