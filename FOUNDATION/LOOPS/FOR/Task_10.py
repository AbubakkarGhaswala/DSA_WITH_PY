# Hello Everyone!
# Task 10 :- Password Retry With Limit Attempts first create a password then try to access it and if wrong Password print "Wrong Password" and again ask for password and  print "You have Exceeded the Number of Attempts"

login_password = '1010'
Attempt = 0
Max_Attempts = 3

for i in range(Max_Attempts):
    user_input = input("Please Enter Your Password :- ")
    
    if user_input == login_password:
        print("Login Successful !!")
        break
    else:
        print("Wrong Password !! Try Again")
        Attempt = Attempt + 1

if Attempt == Max_Attempts:
    print("You have Exceeded the Number of Attempts")
    print("You've Reached Your Attempt Limit Try After 24 Hours!!")
    