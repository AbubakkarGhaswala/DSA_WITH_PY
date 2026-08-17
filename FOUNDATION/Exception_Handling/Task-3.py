# Task 3

# Write a program that asks the user for two integers and performs:

# first number + second number
# first number - second number
# first number × second number
# first number ÷ second number

# Use:

# try
# except ValueError
# except ZeroDivisionError
# else
# finally

# If everything works, else should print:

# All calculations completed successfully.

# And finally should print:

# Program Finished.

try:
    input_1 = int(input("Enter The Value 1 :- "))
    input_2 = int(input("Enter The Value 2 :- "))

    sum_of_two = input_1 + input_2
    Subtract_of_two = input_1 - input_2
    Multiplication_of_two = input_1 * input_2
    division_of_two = input_1 / input_2

    print(f"Addition Of {input_1} & {input_2} is :- {sum_of_two}")
    print(f"Substraction Of {input_1} & {input_2} is :- {Subtract_of_two}")
    print(f"Multiplication Of {input_1} & {input_2} is :- {Multiplication_of_two}")
    print(f"Division Of {input_1} & {input_2} is :- {division_of_two}")
except ValueError:
    print("Heyy User ! You Can Only Enter Integer Values!!")

except ZeroDivisionError:
    print("Heyy User ! Please Don't Enter Value 0 Try With Other Values !!")

except Exception:
    print("Something Went Wrong !! Try Again !!")

else:
    print("All calculations completed successfully.")

finally:
    print("Program Finished.")