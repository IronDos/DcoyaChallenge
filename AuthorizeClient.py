# API Import
from flask.globals import request
from flask_restful import Resource

# Json Web Token
import jwt

# Data
import data

# AuthorizeClient Class
class AuthorizeClient(Resource):
  def get(self):
    # args = authorizeClient_post_args.parse_args()

    if ('JWT' in request.headers and AuthorizeClient.isAuth(request.headers['JWT']) == True):
        print('You are Authorize Client!')
        return {"data": 'You are Authorize Client!'}      
    print('You are not Authorize Client!')
    return {"data": 'You are not Authorize Client!'}
  
  @staticmethod
  def isAuth(jwtString):
    try:
      tempUser = jwt.decode(jwtString, data.jwtSecretKey, algorithms="HS256")
      if (tempUser in data.users):
        return True
    except:
      return False
    return False