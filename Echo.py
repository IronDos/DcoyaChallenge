# API Import
from flask import request
from flask.globals import request
from flask_restful import Resource

import requests, data

# Echo Class
class Echo(Resource):
  def post(self):
    if ('JWT' in request.headers):
      headers = {'JWT': request.headers['JWT']}
      respone = requests.get(data.BASE+'authorizeclient', headers=headers, data='').json()
      if ('data' in respone and respone['data'] != 'You are not Authorize Client!'):
        print('========== Echo ==========')
        print(str(request.data.decode()))
        return {'data': request.data.decode()}

    return {'data': 'You are not Authorize Client!'} 

    