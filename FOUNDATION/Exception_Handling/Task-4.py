# Exception Handling — Task 4 🔥

# Write a program that asks the user to enter two numbers.

# Your program should:

# Convert both inputs to integers.
# Divide the first number by the second.
# Handle ValueError.
# Handle ZeroDivisionError.
# Use else to print:
# Division completed successfully.
# Use finally to print:
# Program Finished.
# Extra challenge 😈

# Inside the try block, also print:

# Both values are valid integers.

# Use only what we've learned so far: try, except, else, finally, ValueError, ZeroDivisionError, and Exception.

# No raise, no file handling, no new concepts.


try :
    input_1 = int(input("Enter The Value 1 :- "))
    input_2 = int(input("Enter The Value 2 :- "))

    
    print("Both values are valid integers.")
    division_of_two = input_1 / input_2
    print(f"Division Of {input_1} & {input_2} is :- {division_of_two}")

except ValueError:
    print("Heyy User ! You Can Only Enter Integer Values!!")

except ZeroDivisionError:
    print("Heyy User ! Please Don't Enter Value 0 Try With Other Values !!")

except Exception:
    print("Something Went Wrong !! Try Again !!")

else:
    print("Division completed successfully.")

finally:
    print("Program Finished.")
    
