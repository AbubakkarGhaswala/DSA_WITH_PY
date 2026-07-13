# Hello everyone and welcome today we are going to create a login page 


username = "Abu.DSA"
password = "DSA@PY"

input_username = input("Enter Username :- ")
input_password = input("Enter Password :- ")

if input_username == "":
    print("Please Enter The Username")
elif input_password == "":
    print("Enter The Password ")
elif username == input_username and password == input_password:
    print("Login Successfully !!")
elif username != input_username and password == input_password:
    print("Invalid Username ")
elif username == input_username and password != input_password:
    print("Invalid Password ")
elif username != input_username and password != input_password:
    print("Invalid username and password")






# Task 6 Done!!