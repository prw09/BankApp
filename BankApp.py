import math
print("Welcome to the Online Bank App")

def SignIn():
  
  global name # username
  global pin # password
  global cb # current balance 
  name = str(input("Please Create Your username: "))
  pin = str(input("Please Create Your 6 digits pin: "))
  cb = str(input("Please Create Your cb: "))

  if len(pin) == 6:
    pin = pin 
  else:
    print("The pin has to be in 6 digits: ")
    newPin = str(input("Please create your 6 digits pin: "))
    if len(newPin) != 6:
      print("The pin has to be in 6 digits: ")
      SignIn()
    else: 
      pin = newPin
  
  print("Thanks for creating this account") 

def forgotPin():
  recoverPin = str(input("Please create your new pin 6 digits pin: "))
  if len(recoverPin) != 6 :
    print("The pin has to be in 6 digits: ")
    forgotPin()
  else:
    print("The new pin has been created, please log in")
    pin = recoverPin

forgotPin()