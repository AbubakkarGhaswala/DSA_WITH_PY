# ==============================================================================
#                 UNDERSTANDING PYTHON LISTS AND TUPLES
# ==============================================================================
# This guide is written in plain, friendly, and easy-to-understand English.
# It covers everything from the absolute basics to tricky edge cases, 
# with real, runnable code examples for every concept.
# ==============================================================================

# ==============================================================================
# 1. WHAT IS A LIST IN PYTHON?
# ==============================================================================
# Imagine a Python List as a dynamic, flexible shopping bag. 
# - You can put anything you want into this bag: apples, books, numbers, or even
#   smaller bags (nested lists).
# - The bag keeps everything in the exact order you put them in (Ordered).
# - You can freely add new items, swap items, or throw items away whenever you 
#   want (Mutable / Changeable).
# - The bag automatically expands when you add items and shrinks when you remove them.

print("--- 1. WHAT IS A LIST? ---")
# Creating a list is simple; we use square brackets []
my_bag = ["apple", "banana", 42, 3.14, True]
print(f"Original list: {my_bag}")
print(f"List length: {len(my_bag)}\n")


# ------------------------------------------------------------------------------
# CORE LIST METHODS & OPERATORS (WITH EDGE CASES)
# ------------------------------------------------------------------------------

# --- A) append(item) ---
# What it does: Adds a single item to the very end of the list.
# Edge Case: If you append another list, it doesn't merge them. It literally
# puts the whole second list inside as a single nested element.
print("--- Method: append() ---")
numbers = [1, 2, 3]
numbers.append(4)
print(f"After appending 4: {numbers}")  # [1, 2, 3, 4]

# Edge case: Appending a list
numbers.append([5, 6])
print(f"After appending [5, 6]: {numbers}")  # [1, 2, 3, 4, [5, 6]]
# (Notice how [5, 6] is treated as a single item at the end!)
print()


# --- B) sort() and C) Reverse Sort ---
# What it does: 
# - .sort() sorts the list in ascending order by default.
# - It is "in-place", meaning it directly changes your original list and returns None.
# - "Reverse sort" is done by passing 'reverse=True' inside .sort().
#
# Edge Case 1: You CANNOT sort a list that contains incompatible types (like integers 
# and strings mixed together, e.g., [1, "apple"]). Python will throw a TypeError.
# Edge Case 2: Sorting is case-sensitive for strings! Uppercase letters come before 
# lowercase letters in the ASCII table (e.g., 'Z' comes before 'a').
# Note: Do not confuse .sort(reverse=True) with .reverse(). 
# - .sort(reverse=True) sorts the list in descending order.
# - .reverse() simply flips the current list backward without sorting it at all.
print("--- Method: sort() & Reverse Sort ---")
scores = [45, 92, 12, 78, 56]

# Standard ascending sort
scores.sort()
print(f"Sorted (Ascending): {scores}")  # [12, 45, 56, 78, 92]

# Descending sort (Reverse sort)
scores.sort(reverse=True)
print(f"Sorted (Descending): {scores}")  # [92, 78, 56, 45, 12]

# Case-sensitive edge case with strings
fruits = ["banana", "Apple", "cherry"]
fruits.sort()
print(f"Sorted strings (Case-sensitive): {fruits}")  # ['Apple', 'banana', 'cherry']
# Tip: To sort alphabetically ignoring case, use: fruits.sort(key=str.lower)
print()


# --- D) insert(index, item) ---
# What it does: Puts an item exactly where you want it. It pushes everything
# after that index one step to the right.
# Edge Case: What if you provide an index that is way too big (out of bounds) 
# or a negative index? 
# - If index is too large (e.g., index 100 on a list of size 3), Python won't crash! 
#   It simply appends the item to the very end.
# - If index is a huge negative number, it puts it at the very beginning (index 0).
print("--- Method: insert() ---")
colors = ["red", "blue"]
colors.insert(1, "green")  # Insert "green" at index 1
print(f"After insert at index 1: {colors}")  # ['red', 'green', 'blue']

# Edge case: Index way out of bounds
colors.insert(999, "gold")
print(f"After inserting at index 999: {colors}")  # ['red', 'green', 'blue', 'gold']

# Edge case: Huge negative index
colors.insert(-999, "silver")
print(f"After inserting at index -999: {colors}")  # ['silver', 'red', 'green', 'blue', 'gold']
print()


# --- E) remove(item) ---
# What it does: Finds the FIRST occurrence of the specified item and deletes it.
# Edge Case: What if the item is not in the list? Python will crash with a ValueError.
# To prevent this, you should always check if the item exists first.
print("--- Method: remove() ---")
pets = ["cat", "dog", "rabbit", "dog"]
pets.remove("dog")
print(f"After removing 'dog' (first occurrence only): {pets}")  # ['cat', 'rabbit', 'dog']

# Edge case: Trying to remove an item that doesn't exist
try:
    pets.remove("dinosaur")
except ValueError as e:
    print(f"Edge Case Error: {e} (You can't remove what isn't there!)")
print()


# --- F) pop(index) ---
# What it does: Removes and returns the item at a specific index. 
# - If you don't provide an index (i.e., list.pop()), it defaults to removing 
#   and returning the very last item.
# Edge Case: If the list is empty, or you give an index that is out of bounds, 
# it will raise an IndexError.
print("--- Method: pop() ---")
tools = ["hammer", "screwdriver", "wrench"]

# Pop without arguments (removes last item)
last_tool = tools.pop()
print(f"Popped item: {last_tool}")  # wrench
print(f"Remaining list: {tools}")    # ['hammer', 'screwdriver']

# Pop with index
first_tool = tools.pop(0)
print(f"Popped item at index 0: {first_tool}")  # hammer
print(f"Remaining list: {tools}")               # ['screwdriver']

# Edge case: Popping from an empty list
empty_list = []
try:
    empty_list.pop()
except IndexError as e:
    print(f"Edge Case Error: {e} (Can't pop from an empty list!)")
print()


# --- G) count(item) ---
# What it does: Counts how many times an item appears in the list.
# Edge Case: If the item doesn't exist, it doesn't crash; it simply returns 0.
print("--- Method: count() ---")
votes = ["yes", "no", "yes", "yes", "maybe"]
print(f"Number of 'yes' votes: {votes.count('yes')}")    # 3
print(f"Number of 'alien' votes: {votes.count('alien')}")  # 0
print()


# --- H) Slicing [start:stop:step] ---
# What it does: Slicing lets you cut out a sub-section of a list.
# - start: The index where the slice begins (inclusive).
# - stop: The index where the slice ends (exclusive - it does NOT include this item).
# - step: How many items to skip (can be negative to go backward!).
#
# Edge Case 1: Out of bounds indices! Unlike normal indexing (like list[999] which crashes),
# slicing is extremely forgiving. If you slice out of bounds, Python just stops at the edge 
# of the list and returns whatever it could find, or an empty list if nothing matches.
# Edge Case 2: Reversing a list with slicing. Using a step of -1 ([::-1]) is a highly 
# popular and extremely fast way to reverse a list or string.
print("--- Concept: Slicing ---")
letters = ["a", "b", "c", "d", "e", "f"]

# Basic slice (index 1 to 4, remember index 4 is excluded)
print(f"Slice [1:4]: {letters[1:4]}")  # ['b', 'c', 'd']

# Slice with steps (every second item)
print(f"Slice [::2]: {letters[::2]}")  # ['a', 'c', 'e']

# Negative indices (start counting from the right side)
print(f"Slice [-3:]: {letters[-3:]}")  # Last 3 items: ['d', 'e', 'f']

# Reverse using slicing
reversed_letters = letters[::-1]
print(f"Reversed list using [::-1]: {reversed_letters}")

# Edge case: Slicing out of bounds (No error!)
print(f"Out of bounds slice [2:999]: {letters[2:999]}")  # ['c', 'd', 'e', 'f']
print(f"Out of bounds slice [999:1000]: {letters[999:1000]}")  # []
print()


# --- I) copy() ---
# What it does: Creates a shallow copy of the list.
# Why it matters: If you write list_b = list_a, you are NOT creating a new list. Both 
# variables are just pointing to the same list in memory. If you change list_b, list_a 
# changes too! Using list_a.copy() gives you a fresh, independent list.
#
# Edge Case: "Shallow" Copy vs "Deep" Copy.
# - .copy() is a SHALLOW copy. It creates a new outer list, but if your list contains
#   nested lists (lists inside lists), the nested lists inside the copy still refer 
#   to the exact same nested lists in the original!
# - If you want a completely independent copy of a nested list, you must use 
#   the copy module's 'deepcopy()' function.
print("--- Method: copy() ---")
original = [1, 2, 3]

# The WRONG way to copy (creating a reference/alias)
alias = original
alias.append(4)
print(f"After modifying alias -> Original: {original}, Alias: {alias}")  # Both are [1, 2, 3, 4]

# The RIGHT way (using .copy())
original = [1, 2, 3]
independent_copy = original.copy()
independent_copy.append(4)
print(f"After modifying independent copy -> Original: {original}, Copy: {independent_copy}")
# Original remains [1, 2, 3], Copy is [1, 2, 3, 4]

# Edge case: Shallow Copy with Nested Lists
nested_original = [[1, 2], [3, 4]]
nested_copy = nested_original.copy()

# Modify the outer list of the copy (independent)
nested_copy.append([5, 6])
# Modify an inner list of the copy (SHARED!)
nested_copy[0][0] = 99

print("\n--- Shallow Copy Edge Case ---")
print(f"Nested Original: {nested_original}")  # [[99, 2], [3, 4]] -> Inner list got changed!
print(f"Nested Copy:     {nested_copy}")      # [[99, 2], [3, 4], [5, 6]]
# To prevent this nested sharing, use: import copy; nested_copy = copy.deepcopy(nested_original)
print("\n" + "="*80 + "\n")

# ==============================================================================
# 2. TRAVERSING IN LISTS (LOOPING THROUGH ITEMS)
# ==============================================================================
# "Traversing" is just a fancy computer science word for "visiting every item in 
# the list one by one." It's like going through your closet and inspecting every
# single shirt you own.
#
# In Python, we have a few different ways to traverse a list using 'for' and 
# 'while' loops. Let's look at each, along with some tricky traps you MUST avoid!

print("--- 2. LIST TRAVERSING ---")
superheroes = ["Batman", "Superman", "Spider-Man", "Wonder Woman"]


# --- Method A: The Direct 'for' Loop (The Most Common Way) ---
# What it does: Directly grabs each item in the list one by one.
# Use this when: You only care about the items themselves and don't care about 
# their index (position) numbers.
print("\n--- Method A: Direct 'for' Loop ---")
for hero in superheroes:
    print(f"Hero: {hero}")

# Edge Case: Traversing an empty list
# If the list is empty, the loop body simply won't run at all. It will not crash!
empty_list = []
for item in empty_list:
    print("This will never print!")


# --- Method B: The Indexed 'for' Loop (using range() and len()) ---
# What it does: Loops through numbers from 0 up to the length of the list, 
# and uses those numbers as indices to access the items.
# Use this when: You need to know the index of each item, or need to access 
# neighboring items (like comparing list[i] with list[i+1]).
print("\n--- Method B: Indexed 'for' Loop ---")
for i in range(len(superheroes)):
    print(f"Index {i} has the hero: {superheroes[i]}")


# --- Method C: The Pythonic Way (using enumerate()) ---
# What it does: Gives you BOTH the index and the item at the same time!
# Use this when: You want clean, readable code that needs both index and value.
print("\n--- Method C: Using enumerate() ---")
for index, hero in enumerate(superheroes):
    print(f"Index {index}: {hero}")


# --- Method D: The 'while' Loop (Manual Control) ---
# What it does: You manually manage a counter variable (usually 'i'), and 
# access items using index as long as the counter is less than the list's length.
# Use this when: You don't want to step through the list sequentially, but instead 
# want to skip items, jump forward/backward based on complex conditions, or loop 
# under custom requirements.
print("\n--- Method D: The 'while' Loop ---")
i = 0
while i < len(superheroes):
    print(f"While Loop - Hero at index {i}: {superheroes[i]}")
    i += 1  # Crucial! If you forget this, you get an infinite loop.


# ==============================================================================
# CRITICAL TRAVERSING TRAPS & EDGE CASES (MUST READ!)
# ==============================================================================

# --- Trap 1: Modifying a list while you are traversing it! ---
# What happens: If you delete or insert elements while looping over a list, Python 
# gets confused because the indices of elements shift dynamically under its feet.
# This causes Python to silently skip elements or check some twice!
print("\n--- Trap 1: Modifying list during iteration (The Bad Way) ---")
numbers = [1, 2, 4, 5, 6]
# Let's say we want to remove all even numbers
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)
print(f"Result (Even number 4 was skipped!): {numbers}")  
# Expected: [1, 5]
# Actual:   [1, 4, 5] (Wait, 4 was skipped because index shifted!)

# The Safe Way: Loop over a COPY of the list using .copy() or [:]
print("--- Trap 1 Solution: Loop over a copy ---")
numbers = [1, 2, 4, 5, 6]
for num in numbers.copy():  # Looping over a fresh copy
    if num % 2 == 0:
        numbers.remove(num)  # Modifying the original list safely
print(f"Safe Result: {numbers}")  # [1, 5] (Correct!)


# --- Trap 2: Neighbor Access Out of Bounds (i+1 or i-1) ---
# What happens: When you try to access the next item (`i + 1`) or previous item (`i - 1`),
# you can easily step outside the boundaries of the list.
# - Accessing `list[i + 1]` on the last item will raise an IndexError.
# - Accessing `list[i - 1]` on the first item (index 0) will access the LAST item 
#   (index -1) instead of throwing an error! This is a silent logic bug.
print("\n--- Trap 2: Neighbor Access & IndexError ---")
prices = [10, 20, 30]

# Let's print each price and its next price
# Incorrect: range(len(prices)) -> Will crash on last item!
# Correct: range(len(prices) - 1) -> Stops one step before the end
for i in range(len(prices) - 1):
    print(f"Price: {prices[i]}, Next Price: {prices[i+1]}")


# --- Trap 3: The 'while' Loop Infinite Loop and Index Crash ---
# If you modify your index counter incorrectly or change list size in a while loop,
# you can easily crash with an IndexError.
print("\n--- Trap 3: While loop Index Crash ---")
items = ["A", "B", "C"]
j = 0
while j < len(items):
    print(f"Inspecting {items[j]}")
    if items[j] == "B":
        items.pop(j)  # Remove "B" -> List size becomes 2!
        # If we just do j += 1, we will skip the next item or crash!
    else:
        j += 1
print(f"Remaining items: {items}")  # ['A', 'C'] (Safely handled!)

print("\n" + "="*80 + "\n")
print("Guide complete! You can run this file directly using Python to see all the outputs.")
