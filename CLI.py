import argparse, requests, data
data.init()

parser = argparse.ArgumentParser(description='RestAPI CLI')
parser.add_argument('-u',help='Please Enter the user name you want to use', required=True)
parser.add_argument('-p',help='Please Enter the password you want to use', required=True)

args = parser.parse_args()

userName = args.u
userPassword = args.p


# Settings
headers = ''
bodyData = {
  'userName': userName,
  'userPassword': userPassword
}
whiteColor = '\u001b[0m'
redColor = '\u001b[31m'
greenColor = '\u001b[32m'

try:
  # Create/Register User
  respone = requests.post(data.BASE + 'register', headers=headers, data=bodyData).json()
  token  = respone['data']

  print(whiteColor + 'Please Enter Action: Echo / Time, for Example:')
  print('TYPING: echo Hello World => will display and return Hello World')
  print('TYPING: time             => will display the current time')
  print('*Press ENTER to send the commands')
  while(True):
    userInput = input('Waiting for input: ')

    headers = {'JWT': token}
    # Echo
    if (userInput.lower().find('echo ' ) == 0):
      bodyData = userInput[5:]
      respone = requests.post(data.BASE+'echo', headers=headers, data=bodyData).json()
      print(greenColor + 'Returned from echo server: ' + respone['data'] + whiteColor)
    # Time
    elif(userInput.lower().find('time' ) == 0):
      respone = requests.get(data.BASE+'time', headers=headers, data='').json()
      print(greenColor + 'Returned from time server: ' + respone['data'] + whiteColor)
    else:
      print(redColor + 'Please enter valid action' + whiteColor)
except:
  print(redColor + '\nError!' + whiteColor)