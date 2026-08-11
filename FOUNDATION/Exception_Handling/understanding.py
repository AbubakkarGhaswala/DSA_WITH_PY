# Python Exception Handling: A Friendly Guide
# --------------------------------------------
# Hey there! Let's understand how Python handles errors (exceptions) so your code doesn't crash 
# when something unexpected happens. 
#
# Think of Exception Handling like a safety net: if your code trips, the net catches it, 
# lets you clean up, and keeps the program running.

"""
Table of Contents:
1. The Basics: What is an Exception?
2. The try-except Block
3. Handling Multiple Specific Exceptions (ValueError, ZeroDivisionError, etc.)
4. The 'else' block
5. The 'finally' block (The clean-up crew)
6. Raising Exceptions manually with 'raise'
7. Quick cheatsheet of common exceptions
"""

# =====================================================================
# 1 & 2. The Basics: try-except
# =====================================================================
print("--- 1 & 2. try-except Basics ---")

# Let's say we want to divide 10 by some user input.
# If we do 10 / 0, Python will throw a ZeroDivisionError and crash.
# We wrap the risky code in a `try` block, and handle the crash in an `except` block.



# =====================================================================
# 3. Handling Multiple Specific Exceptions
# =====================================================================
print("\n--- 3. Handling Multiple Specific Exceptions ---")

# What if a user enters a word instead of a number? Or we get some other error?
# We can chain multiple `except` blocks to handle different situations differently.

def divide_numbers(a, b):
    try:
        # Converting inputs to integers (might raise ValueError if inputs are strings like "hello")
        num1 = int(a)
        num2 = int(b)
        
        # Division (might raise ZeroDivisionError if num2 is 0)
        result = num1 / num2
        print(f"Success! {num1} / {num2} = {result}")
        
    except ZeroDivisionError:
        print("Error: Denominator cannot be zero!")
        
    except ValueError:
        print("Error: Please provide valid integers (no letters or decimals)!")
        
    except Exception as e:
        # This is a wildcard that catches any OTHER error we didn't specify above.
        # It's good practice to keep specific exceptions first and this general one last.
        print(f"An unexpected error occurred: {e}")

# Let's test these cases:
print("Testing with valid numbers (10, 2):")
divide_numbers(10, 2)

print("\nTesting with division by zero (10, 0):")
divide_numbers(10, 0)

print("\nTesting with invalid string ('ten', 2):")
divide_numbers("ten", 2)


# =====================================================================
# 4 & 5. The 'else' and 'finally' Blocks
# =====================================================================
print("\n--- 4 & 5. 'else' and 'finally' Blocks ---")

# Python also gives us 'else' and 'finally':
# - 'else': Runs ONLY if the try block executed successfully without any exceptions.
# - 'finally': Runs ALWAYS, no matter what. Even if the code crashes, returns, or succeeds.
#              This is super useful for clean-up tasks (like closing a file or database connection).

def check_age(age_str):
    try:
        print("\n[TRY] Attempting to convert age...")
        age = int(age_str)
    except ValueError:
        print("[EXCEPT] Oh no! That's not a valid age number.")
    else:
        print(f"[ELSE] Conversion successful! Your age is {age}.")
    finally:
        print("[FINALLY] This runs no matter what! Perfect for closing files or cleanups.")

check_age("25")       # Triggers try -> else -> finally
check_age("twenty")   # Triggers try -> except -> finally


# =====================================================================
# 6. Raising Exceptions Manually (raise)
# =====================================================================
print("\n--- 6. Raising Exceptions (raise) ---")

# Sometimes, the code is technically valid Python, but logically incorrect for our app.
# For example, age cannot be negative. We can manually trigger ("raise") an error.

def register_user(username, age):
    try:
        if age < 0:
            # We raise a ValueError manually
            raise ValueError("Age cannot be negative!")
        if not username:
            # We raise a TypeError or ValueError
            raise ValueError("Username cannot be empty!")
        
        print(f"User {username} (Age: {age}) registered successfully!")
        
    except ValueError as error_message:
        print(f"Registration Failed: {error_message}")

register_user("Alice", -5)
register_user("", 20)
register_user("Bob", 30)


# =====================================================================
# 7. Common Exceptions Cheatsheet
# =====================================================================
"""
Here is a list of common exceptions you'll run into as a developer:

1. ZeroDivisionError:
   Occurs when you try to divide a number by zero.
   Example: 1 / 0

2. ValueError:
   Occurs when a function receives an argument of the correct type but inappropriate value.
   Example: int("abc") -> "abc" is a string (correct type for int constructor), but cannot be converted to number.

3. TypeError:
   Occurs when an operation or function is applied to an object of inappropriate type.
   Example: "hello" + 5 -> You can't add a string and an integer together.

4. IndexError:
   Occurs when you try to access an index that is out of range for a list or tuple.
   Example: my_list = [1, 2]; val = my_list[5]

5. KeyError:
   Occurs when you try to access a key in a dictionary that doesn't exist.
   Example: my_dict = {"name": "Bob"}; val = my_dict["age"]

6. FileNotFoundError:
   Occurs when you try to open or delete a file that doesn't exist.
   Example: open("non_existent_file.txt", "r")
"""

print("\n--- Tutorial Complete! Run this file to see how python handles each scenario. ---")
