# Hello Everyone !
# Our task 6 is to take one input from user and find that is that number is availabile in list
# if yes then print number found and if no then print not found 


numbers = [10,20,30,40,50]


user_input = int(input("Enter A Number :- "))

found = False

for i in numbers:
    if user_input == i:
        found = True

if found == True:
    print("Number Found")
else:
    print("Number Not Found")