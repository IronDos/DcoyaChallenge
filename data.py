# Data
def init():
  global PORT, BASE, users, jwtSecretKey
  PORT = 80
  BASE = 'http://127.0.0.1:' + str(PORT) + '/'
  users = []
  jwtSecretKey = 'secret'