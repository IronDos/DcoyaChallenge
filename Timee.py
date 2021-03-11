# API Import
from flask import Flask
from flask.globals import request
from flask_restful import Resource

from datetime import datetime
import requests, data

# Timee Class
class Timee(Resource):
  def get(self):
    if ('JWT' in request.headers):
      headers = {'JWT': request.headers['JWT']}
      respone = requests.get(data.BASE+'authorizeclient', headers=headers, data='').json()
      if ('data' in respone and respone['data'] != 'You are not Authorize Client!'):
        print('========== Time ==========')
        print(str(datetime.now()))
        return {'data': str(datetime.now())}

    return {'data': 'You are not Authorize Client!'} 
