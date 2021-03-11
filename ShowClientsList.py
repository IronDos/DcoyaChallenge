# API Import
from flask_restful import Resource

# Data
import data

# Register Class
class ShowClientsList(Resource):
  def get(self):
    print('========== Clients List ==========')
    print(data.users)
    return {'ClientsList': data.users}