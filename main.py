import time

print("                Login Page")

username1 = "boon"
password1 = "4033987"
username2 = "purge"
password2 = "purgington"

username1inp = "boon"
username2inp = "4033987"
password1inp = "purge"
password2inp = "purgington"

begin = input(" Are you user 1 or 2?: ")


if begin == "1" or begin == "one" : 
  username1inp = input("Enter your username: ")
  print(username1inp) 
time.sleep(2) 
if begin == "1" or  begin == "one" : 
  password1inp = input("Enter your password: ")
  print(password1inp)


if begin == "2" or begin == "two" : 
  username2inp = input("Enter your username: ")
  print(username2inp)
time.sleep(2)
if begin == "2" or begin == "two" : 
 password2inp = input("Enter your password: ")
 print(password2inp)

if username1inp == username1 and password1inp == password1 :
  print("Welcome", username1)
  time.sleep(0.8)
  print("You are now logged in")
elif username2inp == username2 and password2inp == password2 :
  time.sleep(0.8)
  print("Welcome to the system,", username2)
