# Hello Everyone and welcome today we are going to create a calculator using conditions (if , elif , else) and using arithmatic operators 
# So in this we will take 1 input from user then ask for operation he want to perform 
# after that we will take 2 inputs from user and perform the operation 
# and print the result 


input_1 = int(input("Enter The First Value :- "))

print(" ")

print("Press 1 for Addition ")
print("Press 2 for Subtraction ")
print("Press 3 for Multiplication ")
print("Press 4 for Division ")
print("Press 5 for Modulus ")
print("Press 6 for Power ")
print("Press 7 for Floor Division ")
print("Press 8 for Exit ")

print(" ")

operation = int(input("Enter Number To Perform Operation :- "))


print(" ")

input_2 = int(input("Enter The Second Value :- "))


if operation == 1:
    print("You Choose To Do Addition")
    result = input_1 + input_2
    print(f"The Addition of {input_1} and {input_2} = {result}")
elif operation == 2:
    print("You Choose To Do Subtraction")
    result = input_1 - input_2
    print(f"The Subtraction of {input_1} and {input_2} = {result}")
elif operation == 3:
    print("You Choose To Do Multiplication")
    result = input_1 * input_2
    print(f"The Multiplication of {input_1} and {input_2} = {result}")
elif operation == 4:
    print("You Choose To Do Division")
    result = input_1 / input_2
    print(f"The Division of {input_1} and {input_2} = {result}")
elif operation == 5:
    print("You Choose To Do Modulus")
    result = input_1 % input_2
    print(f"The Modulus of {input_1} and {input_2} = {result}")
elif operation == 6:
    print("You Choose To Do Power")
    result = input_1 ** input_2
    print(f"The Power of {input_1} and {input_2} = {result}")
elif operation == 7:
    print("You Choose To Do Floor Division")
    result = input_1 // input_2
    print(f"The Floor Division of {input_1} and {input_2} = {result}")
elif operation == 8:
    print("Exit")

else:
    print("Invalid Operation")


# Task 7 Done !!