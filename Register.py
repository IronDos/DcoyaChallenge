# API Import
from flask_restful import Resource, reqparse

# Json Web Token
import jwt

# Data
import data

# Args
register_post_args = reqparse.RequestParser()
register_post_args.add_argument("userName", type=str, help="userName")
register_post_args.add_argument("userPassword", type=str, help="userPassword")

# Register Class
class Register(Resource):
  def get(self):
    return {'data': 'Register Page'}
  
  def post(self):
    args = register_post_args.parse_args()
    tempUser = args
    data.users.append(args)
    print('========== Added User ==========')
    print(tempUser)

    return {"data": jwt.encode(tempUser, data.jwtSecretKey, algorithm="HS256")}