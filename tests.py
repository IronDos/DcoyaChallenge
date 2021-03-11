import requests, data
from datetime import datetime
data.init()

# Terminal Colors
whiteColor = '\u001b[0m'
redColor = '\u001b[31m'
greenColor = '\u001b[32m'

# Pass / FAIL Strings
passStr = greenColor + '  Pass'
failStr = redColor + '  Fail'

print('Testing All API, please make sure the server is working => main.py')
try:
  # Register / Create User
  print(whiteColor + 'Testing: /register')
  headers = ''
  bodyData = {
    'userName': 'Asaf',
    'userPassword': 'pass'
  }
  respone = requests.post(data.BASE + 'register', headers=headers, data=bodyData).json()
  token  = respone['data']
  if (token == 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyTmFtZSI6IkFzYWYiLCJ1c2VyUGFzc3dvcmQiOiJwYXNzIn0.grULkK9RqoqYui4S3OsDUWe-oq9hRY7X3rT2pa_RRzQ'):
    print(passStr)
  else:
    print(failStr)



  # ClientsList
  print(whiteColor + 'Testing: /showclientslist')
  respone = requests.get(data.BASE + 'showclientslist', headers='', data='').json()
  if ('ClientsList' in respone and len(respone['ClientsList']) > 0):
    for user in respone['ClientsList']:
      if (user == bodyData):
        print(passStr)
        break
  else:
    print(failStr)



  # AuthorizeClient TRUE
  print(whiteColor + 'Testing: /authorizeclient TRUE')
  headers = {'JWT': token}
  respone = requests.get(data.BASE + 'authorizeclient', headers=headers, data='').json()
  if ('data' in respone and respone['data'] == 'You are Authorize Client!'):
    print(passStr)
  else:
    print(failStr)

  # AuthorizeClient FALSE
  print(whiteColor + 'Testing: /authorizeclient FALSE')
  headers = {'JWT': token + '123'}
  respone = requests.get(data.BASE + 'authorizeclient', headers=headers, data='').json()
  if ('data' in respone and respone['data'] == 'You are not Authorize Client!'):
    print(passStr)
  else:
    print(failStr)



  # Echo Auth Pass
  print(whiteColor + 'Testing: /echo after auth PASS')
  headers = {'JWT': token}
  bodyData = 'test 123 Hello World!!!'
  respone = requests.post(data.BASE + 'echo', headers=headers, data=bodyData).json()
  if ('data' in respone and respone['data'] == 'test 123 Hello World!!!'):
    print(passStr)
  else:
    print(failStr)

  # Echo Auth Fail
  print(whiteColor + 'Testing: /echo after auth Fail')
  headers = {'JWT': token + '123'}
  bodyData = 'test 123 Hello World!!!'
  respone = requests.post(data.BASE + 'echo', headers=headers, data=bodyData).json()
  if ('data' in respone and respone['data'] == 'You are not Authorize Client!'):
    print(passStr)
  else:
    print(failStr)



  # Time Auth Pass
  print(whiteColor + 'Testing: /time after auth PASS')
  headers = {'JWT': token}
  bodyData = ''
  respone = requests.get(data.BASE + 'time', headers=headers, data=bodyData).json()
  if ('data' in respone and str(datetime.now()).find(respone['data'][:10]) != -1):
    print(passStr)
  else:
    print(failStr)

  # Time Auth Fail
  print(whiteColor + 'Testing: /time after auth Fail')
  headers = {'JWT': token + '123'}
  bodyData = ''
  respone = requests.get(data.BASE + 'time', headers=headers, data=bodyData).json()
  if ('data' in respone and respone['data'] == 'You are not Authorize Client!'):
    print(passStr)
  else:
    print(failStr)
except:
  print(redColor + 'Error!' + whiteColor)

print(whiteColor)