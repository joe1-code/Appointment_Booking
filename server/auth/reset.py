import json
import os
from flask import jsonify
import random

#To fetch email from input
def resetPassword(request,Users):
 data=json.loads(request.data)

 if data:
  Email=data['email']
  print(Email)
  #return jsonify({'message': Email})
 #To check if a user exists
  user=Users.query.filter_by(email=Email).first()
  if not user:
            return jsonify({'message': 'not a user'})
  #Generate code          
  code=random.randint(1000,9999)
  return jsonify({'code': code})