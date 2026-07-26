
# ==============================================================================
# 2. WHAT IS A TUPLE IN PYTHON?
# ==============================================================================
# Think of a Python Tuple like a factory-sealed cardboard box.
# - Once you put items inside the box and seal it, you cannot add new items, 
#   remove items, or swap any items (Immutable / Unchangeable).
# - If you absolutely need to change it, you have to tear it open (convert it to a list, 
#   modify it, and convert it back to a tuple), or build a brand-new box from scratch.
#
# Why use Tuples if Lists are so flexible?
# 1. Safety: It guarantees that your data won't accidentally be changed elsewhere in your code.
#    Perfect for coordinates (latitude, longitude), RGB colors (red, green, blue), or database IDs.
# 2. Performance: Tuples are slightly faster and use less memory than lists because Python 
#    doesn't have to prepare for future size changes.
# 3. Dictionary Keys: Because tuples cannot change, they can be used as keys in a dictionary. 
#    Lists cannot!

print("--- 2. WHAT IS A TUPLE? ---")
# Creating a tuple is done using parentheses ()
my_tuple = ("red", "green", "blue")
print(f"My Tuple: {my_tuple}")

# Edge Case: The Single-Item Tuple Trap!
# If you want to make a tuple with just one item, you MUST include a trailing comma.
# If you don't, Python thinks the parentheses are just mathematical and treats it as a normal string/number.
not_a_tuple = ("apple")    # This is just a string!
real_tuple = ("apple",)    # This is a tuple!

print(f"Type of ('apple'): {type(not_a_tuple)}")  # <class 'str'>
print(f"Type of ('apple',): {type(real_tuple)}")  # <class 'tuple'>
print()


# ------------------------------------------------------------------------------
# TUPLE METHODS & OPERATIONS (WITH EDGE CASES)
# ------------------------------------------------------------------------------
# Because tuples cannot be changed, they have very few methods! You won't find 
# .append(), .sort(), or .pop() here. Only search and analysis methods are allowed.

# --- A) count(item) ---
# What it does: Counts how many times an item appears in the tuple.
# Edge Case: Returns 0 if not found (does not crash).
print("--- Tuple Method: count() ---")
numbers_tuple = (1, 2, 3, 2, 4, 2)
print(f"Number of times 2 appears: {numbers_tuple.count(2)}")      # 3
print(f"Number of times 999 appears: {numbers_tuple.count(999)}")  # 0
print()


# --- B) index(item) ---
# What it does: Finds and returns the first index where the item appears.
# - You can optionally pass search bounds: tuple.index(item, start, end).
# Edge Case: If the item is not in the tuple, Python will crash with a ValueError.
print("--- Tuple Method: index() ---")
names_tuple = ("Alice", "Bob", "Charlie", "Bob")

first_bob_index = names_tuple.index("Bob")
print(f"First index of 'Bob': {first_bob_index}")  # 1

# Searching with start/end bounds
second_bob_index = names_tuple.index("Bob", 2)
print(f"Index of 'Bob' starting search from index 2: {second_bob_index}")  # 3

# Edge case: Item not found
try:
    names_tuple.index("David")
except ValueError as e:
    print(f"Edge Case Error: {e} (Cannot find 'David' in the tuple!)")
print()


# --- C) Slicing in Tuples ---
# What it does: Just like lists, you can slice tuples using the [start:stop:step] syntax.
# Why it matters: Slicing a tuple does NOT modify the original tuple. Instead, it 
# returns a BRAND-NEW tuple containing the sliced elements.
print("--- Tuple Concept: Slicing ---")
letters_tuple = ("a", "b", "c", "d", "e", "f")

# Basic slice
print(f"Slice [1:4]: {letters_tuple[1:4]}")  # ('b', 'c', 'd')

# Reverse a tuple using slicing
reversed_tuple = letters_tuple[::-1]
print(f"Reversed tuple using [::-1]: {reversed_tuple}")  # ('f', 'e', 'd', 'c', 'b', 'a')

# Edge case: Out of bounds (works exactly like list slicing - no error!)
print(f"Out of bounds slice [3:99]: {letters_tuple[3:99]}")  # ('d', 'e', 'f')
print()

# ==============================================================================
# SUMMARY OF THE KEY DIFFERENCES:
# ==============================================================================
# Feature          | List [ ]                             | Tuple ( )
# -----------------|--------------------------------------|----------------------
# Mutability       | Mutable (Can change/add/remove)       | Immutable (Locked once created)
# Speed            | Slower (Overhead for resizing)        | Faster (Static memory allocation)
# Methods available| Many (.append, .sort, .pop, etc.)     | Few (.count, .index)
# Use Case         | Dynamic data that changes frequently | Constant data, keys for dictionaries
# ==============================================================================
print("Guide complete! You can run this file directly using Python to see all the outputs.")
