# Import Flask
from flask import Flask
from flask_restful import Api, Resource

# Import APIs
from Register import Register
from ShowClientsList import ShowClientsList
from AuthorizeClient import AuthorizeClient
from Echo import Echo
from Timee import Timee

# Import&Init Data
import data
data.init()

app = Flask(__name__)
api= Api(app)

# Routes and Resources
api.add_resource(Register, '/register')
api.add_resource(ShowClientsList, '/showclientslist')
api.add_resource(AuthorizeClient, '/authorizeclient')
api.add_resource(Echo, '/echo')
api.add_resource(Timee, '/time')


if (__name__ == "__main__"):
  app.run(port=data.PORT, debug=True)