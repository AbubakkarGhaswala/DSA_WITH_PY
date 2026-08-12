# Exception Handling — Task 2 🔥

# Write a program that asks the user to enter a number.

# Your program should:

# Convert the input into an integer.
# Try to calculate:
# 100 / number
# Handle ZeroDivisionError if the user enters 0.
# Handle ValueError if the user enters something like "abc".
# If there is no error, print the result.
# Use else to print:
# Division completed successfully.
# Use finally to print:
# Program Finished.
# Example

# Input:

# 20

# Output:

# Result: 5.0
# Division completed successfully.
# Program Finished.


try :
    user_input = int(input("Please Enter A Value :- "))

    result = 100/user_input

    print(f"Result :- {result}")

except ZeroDivisionError:
    print("Heyy User !! You Can't Divide Number With 0")

except ValueError:
    print("Heyy User !! Kindly Enter Valid Value")

except Exception:
    print("Something Went Wrong !! Please Try Again !!")

else :
    print("Division completed successfully.")
finally :
    print("Program Finished.")