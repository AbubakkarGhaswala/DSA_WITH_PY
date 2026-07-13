# ==============================================================================
# UNDERSTANDING PYTHON DICTIONARIES (A Human-Friendly, Deep Dive)
# ==============================================================================
#
# Imagine you have a physical contact book. To find "John Doe's" phone number, 
# you don't flip through page 1, page 2, page 3... instead, you go straight to 
# the letter 'J', look up "John Doe", and get the number. 
#
# In programming, lists and tuples force you to find things by their position 
# (index 0, 1, 2). But in the real world, we rarely identify things by index. 
# We identify things by names, labels, or IDs.
#
# That is exactly what a Python Dictionary (`dict`) is: a collection of 
# "Key-Value" pairs. 
# - The **Key** is the label (e.g., "John Doe").
# - The **Value** is the data associated with it (e.g., "+1-555-0199").
#
# Let's dive deep into how they work, why they are so fast, and every single 
# method you will ever need to use.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. THE GOLDEN RULES OF DICTIONARIES
# ------------------------------------------------------------------------------
# Before writing code, remember these three rules:
#
# 1. KEYS MUST BE UNIQUE: You can't have two contacts named "John Doe" in the 
#    same dictionary without one overwriting the other. If you assign a value 
#    to an existing key, the old value is gone.
# 2. KEYS MUST BE IMMUTABLE (HASHABLE): Python needs to calculate a fixed number 
#    (a hash) for each key to know where to store it. Therefore, keys must be 
#    things that cannot change, like strings, integers, floats, or tuples. 
#    Lists and other dictionaries cannot be keys!
# 3. VALUES CAN BE ANYTHING: A value can be a list, a set, another dictionary, 
#    a function, or even None. There are no restrictions on values.
# ------------------------------------------------------------------------------

# --- Demonstration of Valid & Invalid Keys ---
# Valid: Strings, Integers, and Tuples as keys
valid_dict = {
    "name": "Alice",      # String key
    42: "The Answer",     # Integer key
    (40.7128, -74.0060): "New York City Coords"  # Tuple key (immutable elements)
}

# Invalid: Attempting to use a List as a key will raise a TypeError: unhashable type: 'list'
try:
    invalid_dict = {["colors"]: ["red", "blue"]}
except TypeError as e:
    print(f"❌ Error: {e} (Lists are mutable and cannot be hashed!)")


# ==============================================================================
# 2. CREATING DICTIONARIES
# ==============================================================================
print("\n--- 2. Creating Dictionaries ---")

# Method A: Literal curly braces (Most common and readable)
user_profile = {
    "username": "coder_99",
    "level": 5,
    "is_active": True
}

# Method B: The dict() constructor (Using keyword arguments)
# Note: Keys are passed as arguments (no quotes needed here), but they become strings.
car = dict(brand="Ford", model="Mustang", year=1964)

# Method C: From a list of tuples (Useful when converting table-like data)
pairs = [("apple", 0.99), ("banana", 0.59), ("orange", 0.79)]
price_lookup = dict(pairs)

# Method D: Dict Comprehension (Dynamic creation)
# Let's create a lookup of numbers and their squares
squares = {x: x**2 for x in range(1, 6)}

print("Squares dictionary:", squares)


# ==============================================================================
# 3. ACCESSING AND MODIFYING VALUES
# ==============================================================================
print("\n--- 3. Accessing & Modifying ---")

# Accessing with square brackets [key]
# WARNING: If the key doesn't exist, Python will crash with a KeyError!
print("Username:", user_profile["username"])

# Accessing safely with .get()
# If the key isn't found, it returns None (instead of crashing).
# You can also provide a default fallback value as the second argument!
print("Bio (defaulting to None):", user_profile.get("bio"))
print("Bio (custom fallback):", user_profile.get("bio", "No bio written yet."))

# Modifying and Adding keys
# The syntax is exactly the same for both. If it exists, it updates. If not, it adds it.
user_profile["level"] = 6            # Updates existing key
user_profile["location"] = "Tokyo"    # Adds new key-value pair

print("Updated Profile:", user_profile)


# ==============================================================================
# 4. EVERY DICTIONARY METHOD: IN-DEPTH EXPLANATIONS & SAMPLES
# ==============================================================================
# Let's look at every built-in method Python dictionaries support.

stock = {
    "apples": 50,
    "bananas": 120,
    "cherries": 15
}

# ------------------------------------------------------------------------------
# Method 1: .keys()
# Returns a "view object" containing all the keys in the dictionary.
# Think of it as a dynamic window. If you update the dictionary, the keys view
# updates automatically!
# ------------------------------------------------------------------------------
print("\n--- Method 1: .keys() ---")
all_keys = stock.keys()
print("Keys view:", all_keys)

# Adding an item dynamically updates the view!
stock["dates"] = 40
print("Keys view after adding 'dates':", all_keys)

# Often converted to a list if you need index-based operations:
keys_list = list(stock.keys())
print("Keys as a list:", keys_list)


# ------------------------------------------------------------------------------
# Method 2: .values()
# Just like .keys(), but returns a dynamic view of all values.
# ------------------------------------------------------------------------------
print("\n--- Method 2: .values() ---")
all_values = stock.values()
print("Values view:", all_values)


# ------------------------------------------------------------------------------
# Method 3: .items()
# Returns a dynamic view of tuples. Each tuple is (key, value).
# This is the industry standard way to loop through dictionaries.
# ------------------------------------------------------------------------------
print("\n--- Method 3: .items() ---")
all_items = stock.items()
print("Items view:", all_items)

# Practical usage: unpacking key and value in a loop
print("Looping through items:")
for fruit, quantity in stock.items():
    print(f" - We have {quantity} {fruit}")


# ------------------------------------------------------------------------------
# Method 4: .get(key, default)
# Accesses a key safely. We discussed this above, but remember it avoids KeyErrors.
# ------------------------------------------------------------------------------
print("\n--- Method 4: .get() ---")
print("Elderberry stock:", stock.get("elderberries", 0))


# ------------------------------------------------------------------------------
# Method 5: .setdefault(key, default)
# Extremely powerful and often misunderstood!
# What it does:
# 1. Checks if the key exists.
# 2. If it DOES exist, it does nothing and returns the existing value.
# 3. If it DOES NOT exist, it inserts the key with the default value and returns it.
# ------------------------------------------------------------------------------
print("\n--- Method 5: .setdefault() ---")
# "apples" already exists with value 50. setdefault will just return 50 and change nothing.
apples_qty = stock.setdefault("apples", 100)
print(f"Apples value returned: {apples_qty}, stock: {stock['apples']}")

# "figs" does NOT exist. setdefault will add "figs": 25 and return 25.
figs_qty = stock.setdefault("figs", 25)
print(f"Figs value returned: {figs_qty}, updated dictionary: {stock}")


# ------------------------------------------------------------------------------
# Method 6: .update(other_dict_or_iterable)
# Merges another dictionary (or an iterable of key-value tuples) into this one.
# Existing keys are overwritten; new keys are added.
# ------------------------------------------------------------------------------
print("\n--- Method 6: .update() ---")
new_deliveries = {"bananas": 150, "grapes": 80}
stock.update(new_deliveries)
print("Stock after bulk update:", stock)


# ------------------------------------------------------------------------------
# Method 7: .pop(key, default)
# Removes the specified key and returns its value.
# If the key is not found, it returns the default value. If no default is provided
# and the key doesn't exist, it raises a KeyError.
# ------------------------------------------------------------------------------
print("\n--- Method 7: .pop() ---")
removed_val = stock.pop("cherries")
print(f"Removed Cherries. Value was: {removed_val}")
print("Stock now:", stock)

# Pop with fallback to prevent crashes:
removed_safe = stock.pop("blueberries", "Not found in stock")
print("Trying to pop blueberries:", removed_safe)


# ------------------------------------------------------------------------------
# Method 8: .popitem()
# Removes and returns the LAST inserted key-value pair as a tuple: (key, value).
# Useful for implementing LIFO (Last-In, First-Out) stack behavior.
# In Python versions before 3.7, it popped a random item!
# ------------------------------------------------------------------------------
print("\n--- Method 8: .popitem() ---")
last_item = stock.popitem()
print(f"Popped last item: {last_item}")
print("Stock now:", stock)


# ------------------------------------------------------------------------------
# Method 9: .clear()
# Deletes everything inside the dictionary, leaving it empty.
# ------------------------------------------------------------------------------
print("\n--- Method 9: .clear() ---")
temp_stock = stock.copy()  # Creating a copy first to clear it
print("Before clear:", temp_stock)
temp_stock.clear()
print("After clear:", temp_stock)


# ------------------------------------------------------------------------------
# Method 10: .copy()
# Returns a shallow copy of the dictionary.
# Why is this needed? If you just write `dict2 = dict1`, they both point to the
# SAME object in memory. Modifying dict2 would also modify dict1!
# ------------------------------------------------------------------------------
print("\n--- Method 10: .copy() ---")
original = {"a": [1, 2], "b": 3}

# Reference vs Copy Comparison
ref_only = original          # Points to the exact same dictionary
copied = original.copy()     # Creates a new dictionary container

# Modifying the copy container:
copied["c"] = 99
print("Original keys:", list(original.keys()))  # Unaffected!
print("Copied keys:", list(copied.keys()))      # Has 'c'!

# WARNING ON SHALLOW COPY:
# A shallow copy duplicates the dictionary structure, but not nested mutable objects (like lists).
# If you modify a list inside the copy, it will affect the original too!
copied["a"].append(3)
print("Original nested list:", original["a"])  # Output is [1, 2, 3]!
# (To prevent this, use `copy.deepcopy()` from Python's standard `copy` library).


# ------------------------------------------------------------------------------
# Method 11: .fromkeys(sequence, value)
# A class method used to create a new dictionary with keys from a sequence
# (like a list or tuple) and all values set to the same initial value.
# Defaults to None if no value is specified.
# ------------------------------------------------------------------------------
print("\n--- Method 11: .fromkeys() ---")
users = ["alice", "bob", "charlie"]
# Initialize everyone with 0 points
points_leaderboard = dict.fromkeys(users, 0)
print("Initialized Leaderboard:", points_leaderboard)


# ==============================================================================
# 5. USEFUL DICTIONARY TRICKS & TIPS
# ==============================================================================
print("\n--- 5. Tips and Tricks ---")

# Trick 1: Membership Testing (using "in")
# This is incredibly fast (O(1) average complexity).
# It checks if a KEY is present in the dictionary.
inventory = {"swords": 3, "shields": 1, "potions": 10}

if "swords" in inventory:
    print("⚔️ Ready for battle! Swords found.")

# Note: "in" checks KEYS, not values.
if 10 in inventory:
    print("This won't print because 10 is a value, not a key.")
else:
    print("Value '10' is not found using 'in' (only keys are checked!).")


# Trick 2: Iteration Shortcuts
# By default, iterating over a dictionary directly loops through its KEYS.
print("Looping directly over dictionary:")
for key in inventory:
    print(f"Key: {key} -> Value: {inventory[key]}")


# Trick 3: Merging Dictionaries (Python 3.9+)
# You can use the union operator `|` to merge two dictionaries into a new one.
dict_a = {"x": 1, "y": 2}
dict_b = {"y": 99, "z": 4}  # 'y' is duplicate

merged = dict_a | dict_b
print("Merged dictionary using | (Python 3.9+):", merged)
# Notice 'y' took the value from dict_b (the right-hand side operand wins).


# ==============================================================================
# 6. UNDER THE HOOD: HOW DICTIONARIES WORK SO FAST (O(1))
# ==============================================================================
#
# If you have 1,000,000 items in a list, finding one item can take up to 
# 1,000,000 checks (O(N) time complexity).
# If you have 1,000,000 items in a dictionary, looking up a key takes roughly 
# ONE step (O(1) time complexity).
#
# How?
#
# 1. Hashing: When you do `my_dict["name"] = "Alice"`, Python runs the key
#    "name" through a hashing function: `hash("name")`. This turns the string 
#    into a unique number.
# 2. Index Mapping: That number is mapped directly to a specific slot in an internal
#    array/memory list.
# 3. Direct Lookup: When you ask for `my_dict["name"]`, Python hashes "name" again,
#    goes straight to that index, and grabs "Alice". No searching needed!
#
# This makes dictionaries one of the most powerful and essential data structures
# in computer science.
# ==============================================================================
