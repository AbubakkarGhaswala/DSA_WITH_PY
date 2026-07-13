# Hello Everyone 
# So basically here we have to build aatm App in which there is a customer 
# So user will come in atm and will enter pin 
# If pin is correct then he will be able to access the atm 
# If pin is incorrect then he will not be able to access the atm 
# In total 3 chances will be given to user to enter pin 
# and if he enter pin correctly then he will be able to access the atm 
# and if he enter pin incorrectly then he will not be able to access the atm 
# and if he enter pin incorrectly 3 times then he will not be able to access the atm 
# and if he enter pin correctly 1st time then he will be able to access the atm 
# and if he enter pin correctly 2nd time then he will be able to access the atm 
# and if he enter pin correctly 3rd time then he will be able to access the atm 
# and then he can do following operations 
# 1. Check Balance
# 2. Withdraw Money
# 3. Deposit Money
# 4. Change Pin
# 5. Exit

Pin = 1234
Balance = 5000

verify_pin = int(input("Please Enter Your Pin :- "))

if verify_pin == Pin :
    print("Your Pin Is Correct You May Proceed With Following Options which display below :- ")
    print(" ")
    print("Press 1 for Check Balance")
    print(" ")
    print("Press 2 For Withdrawal Money")
    print(" ")
    print("Press 3 For Deposite Money")
    print(" ")
    print("Press 4 For Change Pin")
    print(" ")
    print("Press 5 For Exit")

    select_option = int(input("Press from 1 to 5 to perfom task :- "))

    if select_option == 1:
        print(Balance)
    elif select_option == 2:
        input_for_withdraw = int(input("Enter The Amount You Want To Withdraw :- "))
        if input_for_withdraw <= 0:
            print("Please Enter Valid Amount To Withdrawal")

        elif input_for_withdraw < Balance:
            print(f"Your Amount Has Been Withdrawn {input_for_withdraw}")
            Balance = Balance - input_for_withdraw
            print(f"Your Remain Balance Is :- {Balance}")
            print("Thank You!!")
        
        elif input_for_withdraw > Balance:
            print(f"Please Enter Withdraw Amount Request Within {Balance} This Amount")
    elif select_option == 3:
        input_for_deposite = int(input("Enter The Amount You Want To Deposit :- "))

        if input_for_deposite <= 0:
            print("Please Enter Valid Amount To Deposit")
        else :
            Balance = Balance + input_for_deposite
            print(f"You Have Deposit {input_for_deposite} Rupees ! ")
            print(f"Your Balance Is Now {Balance}")
            print("Thank You !!")
    elif select_option == 4:
        print("You Have Select The Option Of Change Pin!!")

        old_pin_input = int(input("Please Enter Your Old Pin:- "))

        if old_pin_input == Pin:

            new_pin_input = int(input("Please Enter New Pin:- "))

            Pin = new_pin_input

            print("Thank You !! Your Pin Has Been Change!")
        elif old_pin_input != Pin:
            print("You've Enter Wrong Pinn !!") 

    elif select_option == 5:
        print("--------------- Exit -------------") 

    elif select_option > 5 :
        print("Invalid Key Pressed !!")  

elif Pin != verify_pin:
    print("Wrong Pin Enter !!!")