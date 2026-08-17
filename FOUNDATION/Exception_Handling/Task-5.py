# Exception Handling — Boss Task

# Build a Simple Calculator using everything you've learned.

# The program should:

# Ask the user for two numbers.

# Ask the user to choose an operation:

# +  → Addition
# -  → Subtraction
# *  → Multiplication
# /  → Division
# Perform the selected operation.
# Handle:
# ValueError → invalid number input
# ZeroDivisionError → division by zero
# Exception → unexpected errors

# Use else to print:

# Calculation completed successfully.

# Use finally to print:

# Calculator closed.
# Example
# Enter first number: 20
# Enter second number: 5
# Enter operation: /


# Result: 4.0
# Calculation completed successfully.
# Calculator closed.

# Important: Don't use anything we haven't learned yet. No raise, no functions, no file handling.

# Build it yourself and send me the code. 😈


try :
    input_1 = int(input("Enter The Value 1 :- "))
    input_2 = int(input("Enter The Value 2 :- "))

    print("Select Your Operation")
    print("1 → Addition")
    print("2 → Subtraction")
    print("3 → Multiplication")
    print("4 → Division")

    operation = int(input("Choose operation (1-4): "))

    if operation == 1:
        sum_of_two = input_1 + input_2
        print(f"You've Selected Addition :- {sum_of_two}")
        
    elif operation == 2:
        subtraction_of_two = input_1 - input_2
        print(f"You've Selected Subtraction :- {subtraction_of_two}")
    elif operation == 3:
        multiplication_of_two = input_1 * input_2
        print(f"You've Selected Multiplication :- {multiplication_of_two}")
    elif operation == 4:
        division_of_two = input_1 / input_2
        print(f"You've Selected Division :- {division_of_two}")
    else:
        print("Invalid operation selected.")

except ValueError:
    print("Invalid input. Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except Exception:
    print(f"An unexpected error occurred ")

else :
    print("Calculation completed successfully.")

finally :
    print("Calculator closed.")