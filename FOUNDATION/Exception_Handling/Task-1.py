# Exception Handling — Task 1

# Write a program that asks the user to enter two numbers and divides the first number by the second.

# Requirements:

# Use try and except.
# Handle ZeroDivisionError.
# Handle ValueError.
# If the division succeeds, print the result.
# Use finally to print:
# Program Finished
# Example

# If user enters:

# 10
# 2

# Output:

# Result: 5.0
# Program Finished

# If user enters:

# 10
# 0

# Output should show your zero-division error message, followed by:

# Program Finished


user_input_1 = int(input("Enter first value :- "))
user_input_2 = int(input("Enter second value :- "))

try :
    result = user_input_1/user_input_2
    print(f"Result :- {result}")

except ZeroDivisionError:
    print("Heyy User !! You Can't Divide Number With 0")

except ValueError:
    print("Heyy User !! Kindly Enter Valid Value")

except Exception:
    print("Something Went Wrong !! Please Try Again !!")

finally:
    print("Program Run Successfully !!")

