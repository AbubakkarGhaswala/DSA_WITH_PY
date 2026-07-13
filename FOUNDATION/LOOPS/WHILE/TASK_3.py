# Hello Everyone Our task 3 is about asking user for enter password this loop will continuously asking for password till 
# user enter the corrcet one using while loop


correct_pass = "Surat@123"

while True:
    input_pass = input("Please Enter Your Password :- ")
    if input_pass == correct_pass:
        print("Passord Correct !!")
        break
    else :
        print("Wrong Password ! Try Again")


print("Loop End")