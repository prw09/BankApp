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


def depositInterest(p, r, t):

  p = float(p)
  r = float(r)
  t = float(t)
  rt = r * t
  e = math.exp(rt)

  #  Compound interest formula
  a = p * e
  return a

print(depositInterest(1000, 0.033, 6))


def Login():

  name1 = str(input("Enter Your Name: "))
  pin1 = str(input("Enter Your Pin: "))
  # check if the name and pin is matched with registered details
  if name1 == name and pin1 == pin:
    print("Welcome to the online bankApp" + " "+ name)
    print("please choose the menu down here!")

  
  else:
      print("Either of your username or pin is wrong")
      print("Please enter valid details!")
      list1 = ["1-yes", "2-no"]
      for i in list1:
        print(i)
      inp = int(input("Enter your choice below"))
      if inp == 1:
        list2 = ["1-do you want to attempt to login again"]
        for e in list2:
          print(e)
        theanswer = str(input("Please enter your choice"))
        theanswer = int(theanswer)

        if theanswer == 1:
          Login()

        elif theanswer == 2:
          forgotPin() 

        else: 
          print("option not available")
          Login() 
      
      elif inp == 2:
        print("Please create your account!")
        SignIn()