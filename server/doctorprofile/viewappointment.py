from flask import jsonify
import json

from ..helper import profile_serializer,appointments_serializer
def getappointment(Appointment):
    pages_perpage = 100
    page = 1
    appointments = Appointment.query.filter_by().order_by(
        Appointment.created.desc())
    if appointments:
       data = [*map(appointments_serializer, appointments)]
       return {'data': data}
    return jsonify({'message' : 'Appointments not found'}),403
