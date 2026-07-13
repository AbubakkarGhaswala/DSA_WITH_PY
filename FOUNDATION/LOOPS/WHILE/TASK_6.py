#  Task 6 — Advanced ATM System Using While Loop
# Build a continuously running ATM system.
# Your ATM should behave like a small real application.
# MAIN REQUIREMENTS
# 1. Login System
# Store:
# ATM PIN
# Initial Balance
# User must enter PIN to access ATM.
# If PIN is incorrect:
# show error message
# ask again
# ATM should continue asking until:
# correct PIN entered
# OR maximum attempts reached
# 2. Maximum PIN Attempts
# User gets ONLY 3 attempts.
# After 3 wrong attempts:
# block access
# terminate ATM system
# 3. ATM Menu
# After successful login, display menu repeatedly.
# Menu options:
# Check Balance
# Withdraw Money
# Deposit Money
# Change PIN
# Exit
# 4. Check Balance
# Display current balance clearly.
# 5. Withdraw Money
# Ask user:
# withdrawal amount
# Conditions to handle:
# amount must be greater than 0
# amount must not exceed balance
# balance should update after successful withdrawal
# Show:
# withdrawn amount
# remaining balance
# 6. Deposit Money
# Ask user:
# deposit amount
# Conditions:
# amount must be greater than 0
# After deposit:
# update balance
# show updated balance
# 7. Change PIN
# Ask:
# current PIN
# new PIN
# Conditions:
# current PIN must match existing PIN
# new PIN must be:
# either 4-digit OR 6-digit
# numeric only
# After successful change:
# update PIN
# show success message
# 8. Exit System
# When user selects Exit:
# display goodbye message
# stop ATM completely
# 9. Invalid Menu Option
# If user enters invalid menu number:
# show proper error message
# return to menu
# 10. Loop Behavior
# ATM must continue running until:
# user exits
# OR
# account gets blocked after failed PIN attempts
# Program should NOT close after one operation.
# IMPORTANT EDGE CASES
# Your ATM should properly handle:
# negative values
# zero values
# invalid menu choices
# wrong PIN
# invalid withdrawal
# invalid deposit
# invalid PIN format
# BONUS FEATURES (Optional — Do if you want stronger logic practice)
# 1. Transaction History
# Store and display:
# deposits
# withdrawals
# 2. Fast Cash
# Options like:
# 500
# 1000
# 2000
# 3. Mini Statement
# Display:
# current balance
# recent transaction
# 4. Account Lock Message
# After 3 failed attempts:
# show security message
# IMPORTANT RULES
# Do NOT:
# rush
# copy from internet
# ask for full solution immediately
# Build:
# step by step
# test each feature separately
# debug carefully
# This task is your first REAL mini application.


from enum import verify
login_password = 1010
balance = 50000
attempt = 0

old_pin_attempt = 0
can_change_pin = True

while True:
    password_input = int(input("Please Enter Your Pin:- "))
    if password_input == login_password:
        print("You've Enter Correct Password You May Proceed With Following Options:-")

        while True:
            print("Menu Options :-")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Change PIN")
            print("5. Exit")

            menu = int(input("Please select an option from the menu :- "))
            if menu == 1:
                print("You Have Selected Check Balance !")
                print(f"Here's Your Balance :- {balance}")
            elif menu == 2:
                print("You've Selected Withdraw Money!!")
                while True:
                    print("Press 1 For Go Back To Menu !!")
                    Withdraw_money = int(input("Enter The Amount You Would Like To Withdrawal :- "))

                    if Withdraw_money <= 0:
                        print("Please Enter Valid Amount..")
                    elif Withdraw_money == 1:
                        break
                    elif Withdraw_money < 100:
                        print("Please Enter Amount More Than 100!!")

                    elif Withdraw_money > 100 and Withdraw_money < balance:
                        balance = balance - Withdraw_money
                        print(f"You've Withdrawal {Withdraw_money} Rupees ! Your Remaining Balance Is {balance}")
                        break
                    
                    elif Withdraw_money > balance:
                        print(f"Please Enter Amount Less Than Your Balance :- {balance} !")
            
            elif  menu == 3:
                print("You've Selected Deposite Money !!")
                while True:
                    print("Press 1 To Go Back To Menu!!")
                    Deposite_input = int(input("Please Enter Amount You Would Like To Deposit:- "))

                    if Deposite_input <= 0:
                        print("Please Enter Valid Amount..")
                    elif Deposite_input == 1:
                        break
                    elif Deposite_input < 100:
                        print("Please Enter Amount More Than 100 Ruppes!!")
                    elif Deposite_input > 100 :
                        balance = balance + Deposite_input
                        print(F"You've Deposite {Deposite_input} Rupees !! ")
                        print(f"Your Updated Balance :- {balance}")
                        break
            
            elif menu == 4:
                print("You've Selected Change Pin")
                while True:

                    if can_change_pin == False:
                        print("Change Pin Access Blocked ! Cause You Have Reached Your limit !")
                        break
                    else :
                        
                        old_pin = int(input("Please Enter Your Old Pin:- "))

                        if old_pin == login_password:
                            print("You've Enter Correct Pin!!!")
                            new_pin = int(input("Please Enter New Pin:- "))
                            verify_new_pin = int(input("Please Re-Enter New Pin:- "))

                            if new_pin == verify_new_pin:
                                login_password = new_pin
                                print("Congratulations !! 🥳 Your Pin Has Been Changed !!")
                                break
                        elif old_pin != login_password:
                            print("Please Enter corrcet Pin!!")
                            old_pin_attempt = old_pin_attempt + 1

                            if old_pin_attempt == 3:
                                print("Sorry ! 😞 You Have Hit 3 Attempts For Today ! Try After 24 Hours")
                                can_change_pin = False
                                break
            elif menu == 5:
                print("Good Byee !!")
                break
            



                    
            

    else :
        attempt = attempt + 1
        if attempt == 3:
            print("Sorry ! 😞 You Have Hit 3 Attempts For Today ! Try After 24 Hours")
            break