"""
================================================================================
MASTERING STRINGS IN PYTHON: UNDER-THE-HOOD, SLICING, INDEXING & METHODS
================================================================================
A comprehensive, deeply informative, and runnable laboratory designed to teach 
Python strings from core memory structures up to advanced algorithmic use.

Written for: Deep DSA and Python Core Understanding
================================================================================
"""

import sys

# ================================================================================
# SECTION 1: UNDER-THE-HOOD MEMORY & ARCHITECTURE
# ================================================================================

"""
--- 1.1 Immutability ---
In Python, strings (`str`) are IMMUTABLE. Once a string object is created in memory, 
its characters cannot be altered, appended, or deleted. 
- Any operation that "modifies" a string (like .replace(), .upper(), or concatenation) 
  actually allocates a BRAND NEW string object in memory.
- Why? 
  1. Hashability: Since strings are immutable, their hash value never changes. This 
     makes them safe to use as keys in dictionaries and elements in sets.
  2. Security/Safety: Sharing string paths, usernames, or database URLs across 
     threads is safe because no part of the program can mutate them mid-execution.
  3. Memory Efficiency: Python can optimize memory storage using "String Interning".

--- 1.2 String Interning ---
For performance, Python automatically caches (interns) short, compile-time string 
constants (typically strings containing only alphanumeric characters and underscores). 
- If you create two identical interned strings, they point to the EXACT same memory address.
- You can manually force interning using `sys.intern(string)`.
"""

def demonstrate_memory_and_interning():
    print("\n--- 1.1 & 1.2 String Immutability & Interning ---")
    
    # Proving Immutability
    s1 = "hello"
    try:
        s1[0] = 'H'  # Will raise a TypeError
    except TypeError as e:
        print(f"  Attempted s1[0] = 'H' -> Caught Expected Error: {e}")
        
    # Automatic Interning
    a = "python_dsa"
    b = "python_dsa"
    print(f"  a = '{a}', b = '{b}'")
    print(f"  Identity check (a is b): {a is b} (Both point to ID: {id(a)})")
    
    # Strings with spaces are typically NOT auto-interned at runtime if built dynamically
    c = "".join(["hello", " world"])
    d = "".join(["hello", " world"])
    print(f"  c = '{c}', d = '{d}'")
    print(f"  Value check (c == d): {c == d}")
    print(f"  Identity check (c is d): {c is d} (Different memory addresses: {id(c)} vs {id(d)})")
    
    # Manual Interning
    c_interned = sys.intern(c)
    d_interned = sys.intern(d)
    print(f"  After sys.intern(): Identity check (c is d): {c_interned is d_interned}")


"""
--- 1.3 PEP 393: Flexible String Representation ---
Under the hood (since Python 3.3), Python doesn't use a fixed width (like 2 or 4 bytes) 
for all characters in a string. Instead, Python dynamically adapts the storage type 
based on the "maximum character" in the string to conserve RAM:
  1. Latin-1 / ASCII (characters up to U+00FF): 1 byte per character.
  2. UCS-2 (characters up to U+FFFF, e.g., most alphabets, symbols): 2 bytes per character.
  3. UCS-4 (characters up to U+10FFFF, e.g., Emojis): 4 bytes per character.
"""

def demonstrate_flexible_representation():
    print("\n--- 1.3 PEP 393 Memory Usage Demo ---")
    # All strings have the same length (5 characters) but use different byte representations.
    ascii_str = "hello"       # 1 byte/char
    greek_str = "αβγδε"       # 2 bytes/char
    emoji_str = "🐍🔥🚀👽💻"   # 4 bytes/char
    
    print(f"  ASCII: '{ascii_str}' (len={len(ascii_str)}) -> Size in memory: {sys.getsizeof(ascii_str)} bytes")
    print(f"  Greek: '{greek_str}' (len={len(greek_str)}) -> Size in memory: {sys.getsizeof(greek_str)} bytes")
    print(f"  Emoji: '{emoji_str}' (len={len(emoji_str)}) -> Size in memory: {sys.getsizeof(emoji_str)} bytes")


# ================================================================================
# SECTION 2: INDEXING & SLICING (THE DNA OF STRING NAVIGATION)
# ================================================================================

"""
--- 2.1 Indexing: Positive & Negative ---
Strings are sequence types. Every character has a specific slot (index).
- Positive Indexing: Starts at `0` from the left, goes to `len(s) - 1`.
- Negative Indexing: Starts at `-1` from the right, goes to `-len(s)`.

   String:   P    y    t    h    o    n
   Pos Idx:  0    1    2    3    4    5
   Neg Idx: -6   -5   -4   -3   -2   -1

*Edge Case/Gotcha*: Accessing an index outside of these ranges raises an `IndexError`.
"""

def demonstrate_indexing():
    print("\n--- 2.1 Indexing Demo ---")
    s = "Python"
    print(f"  String: '{s}', length: {len(s)}")
    print(f"  Positive Index s[0]: {s[0]}  | Negative Index s[-6]: {s[-6]}")
    print(f"  Positive Index s[5]: {s[5]}  | Negative Index s[-1]: {s[-1]}")
    
    # Out of Bounds check
    try:
        _ = s[10]
    except IndexError as e:
        print(f"  Accessing s[10] -> Caught Expected Error: {e}")


"""
--- 2.2 Slicing: [start:stop:step] ---
Slicing extracts a substring. The general syntax is `s[start:stop:step]`.
- start: The index where slicing begins (inclusive). Defaults to `0` if step > 0.
- stop: The index where slicing ends (exclusive). Defaults to `len(s)` if step > 0.
- step: The step/stride size. Defaults to `1`.

*Crucial Edge Case (Fault Tolerance)*: Unlike indexing, slicing is highly resilient. 
If start or stop are out of bounds, Python does NOT raise an error. It gracefully 
clamps the bounds to the string boundaries.

--- 2.3 Slicing with Negative Steps ---
When `step` is negative:
  - The slice traverses BACKWARDS (right to left).
  - Defaults change: `start` defaults to `-1` (end of string), `stop` defaults to 
    the virtual index before the start of the string (beginning).
  - Formula: You must ensure `start` is to the right of `stop` (i.e. start > stop 
    in index value), otherwise you will get an empty string.
"""

def demonstrate_slicing():
    print("\n--- 2.2 & 2.3 Slicing & Negative Steps Demo ---")
    s = "DataStructures"
    
    # Standard Slicing
    print(f"  Original: '{s}'")
    print(f"  s[0:4]:   '{s[0:4]}'   (Indices 0, 1, 2, 3)")
    print(f"  s[4:10]:  '{s[4:10]}'  (Indices 4 to 9)")
    print(f"  s[::2]:   '{s[::2]}'   (Every second character)")
    
    # Graceful Clamping (Out of bounds)
    print(f"  Out of bounds slice s[5:100]: '{s[5:100]}' (No crash!)")
    
    # Negative Step Slicing (Reversing)
    print(f"  Reversing with s[::-1]: '{s[::-1]}'")
    
    # Tricky Negative Step Bounds
    # Remember: start must be higher/to-the-right of stop to slice backwards!
    # Let's slice 'Struct' backwards. 'Struct' starts at index 4 ('S') and ends at 9 ('t') -> 'Structure'
    # To slice 'Struct' (indices 4 to 9) backwards, we start at 9 ('u') and go down to 4 ('S').
    # Since stop is exclusive, to include index 4, we must set stop to 3.
    print(f"  Backwards slice s[9:3:-1]: '{s[9:3:-1]}' (Slices 'tcurtS' backwards)")
    print(f"  Incorrect backwards slice s[3:9:-1]: '{s[3:9:-1]}' (Returns empty string because start < stop)")


# ================================================================================
# SECTION 3: DEEP DIVE INTO REQUESTED STRING METHODS
# ================================================================================

"""
--- 3.1 endswith(suffix[, start[, end]]) ---
Checks if the string ends with the specified suffix. Returns True or False.
- start/end parameters restrict the search to a specific substring slice.
- Edge Case / Trick: You can pass a TUPLE of strings to suffix. If the string 
  ends with *any* of the suffixes in the tuple, it returns True. Very useful for 
  checking file extensions.
"""

def demonstrate_endswith():
    print("\n--- 3.1 endswith() Demo ---")
    filename = "report_dsa.pdf"
    
    print(f"  Does '{filename}' end with '.pdf'? : {filename.endswith('.pdf')}")
    print(f"  Does it end with '.docx'?         : {filename.endswith('.docx')}")
    
    # Multi-suffix check using a tuple (Crucial Pattern!)
    extensions = (".png", ".jpg", ".jpeg", ".pdf")
    print(f"  Does it end with any of {extensions}? : {filename.endswith(extensions)}")
    
    # With start/end parameters (bounds restricted to 'report_dsa')
    # index range 0 to 10 is 'report_dsa'
    print(f"  Does slice s[0:10] end with '_dsa'? : {filename.endswith('_dsa', 0, 10)}")


"""
--- 3.2 count(sub[, start[, end]]) ---
Returns the number of non-overlapping occurrences of substring `sub`.
- Edge Case / Gotcha: It only counts *non-overlapping* matches. 
  Example: In 'aaaa', counting 'aa' yields 2, NOT 3!
- Edge Case: If searching for an empty string `""`, Python counts the gaps 
  between characters, returning `len(s) + 1`.
"""

def demonstrate_count():
    print("\n--- 3.2 count() Demo ---")
    s = "banana"
    print(f"  Occurrence of 'an' in '{s}': {s.count('an')}")
    
    # The Overlap Gotcha
    overlap_str = "aaaa"
    print(f"  Counting 'aa' in '{overlap_str}': {overlap_str.count('aa')} (Non-overlapping only!)")
    
    # Empty string search gotcha
    print(f"  Counting empty string '' in 'abc': {'abc'.count('')} (Calculated as len + 1)")


"""
--- 3.3 find(sub[, start[, end]]) vs index(sub) ---
Both locate the index of the first occurrence of substring `sub`.
- Difference / Gotcha:
  - `find()` returns `-1` if the substring is not found.
  - `index()` raises a `ValueError` if the substring is not found.
- In DSA coding, use `find()` when a missing substring is a normal occurrence 
  that requires fallback logic. Use `index()` if the missing substring indicates 
  a failure state or error.
"""

def demonstrate_find_and_index():
    print("\n--- 3.3 find() vs index() Demo ---")
    s = "learning_python"
    
    print(f"  Using find() for 'python': {s.find('python')}")
    print(f"  Using find() for 'java' (not found): {s.find('java')} (Returns -1)")
    
    print(f"  Using index() for 'python': {s.index('python')}")
    try:
        _ = s.index('java')
    except ValueError as e:
        print(f"  Using index() for 'java' (not found) -> Caught Expected ValueError: {e}")


"""
--- 3.4 replace(old, new[, count]) ---
Returns a COPY of the string with all occurrences of `old` replaced by `new`.
- Third argument `count` restricts how many occurrences from the left are replaced.
- Remember: Because strings are immutable, the original string is completely untouched!
"""

def demonstrate_replace():
    print("\n--- 3.4 replace() Demo ---")
    s = "apple apple apple banana"
    print(f"  Original: '{s}'")
    
    # Replace all
    replaced_all = s.replace("apple", "orange")
    print(f"  Replaced all: '{replaced_all}'")
    
    # Replace with max count limit
    replaced_limited = s.replace("apple", "orange", 2)
    print(f"  Replaced only 2: '{replaced_limited}'")
    print(f"  Verify original is unchanged: '{s}'")


"""
--- 3.5 capitalize() vs title() vs upper() vs lower() ---
Case mapping properties:
- `capitalize()`: Converts ONLY the very first character of the string to uppercase, 
  and converts ALL other characters to lowercase.
- `title()`: Capitalizes the first character of every word (space separated), but can 
  have strange behaviors (e.g. "it's" -> "It'S").
- `upper()` / `lower()`: Converts all characters to uppercase or lowercase.
"""

def demonstrate_capitalize_and_case():
    print("\n--- 3.5 capitalize() and Case Methods Demo ---")
    s = "tHe qUicK bRoWn FoX."
    print(f"  Original:    '{s}'")
    print(f"  capitalize(): '{s.capitalize()}' (Only index 0 upper, rest forced lower)")
    print(f"  title():      '{s.title()}' (First char of words upper)")
    print(f"  upper():      '{s.upper()}'")
    print(f"  lower():      '{s.lower()}'")


# ================================================================================
# SECTION 4: PERFORMANCE GOTCHAS IN DSA (STRING BUILDER PATTERN)
# ================================================================================

"""
--- 4.1 Concatenation Complexity ---
Because strings are immutable, writing a loop that builds a string character-by-character 
via `s += char` has O(N^2) time complexity! 
Every iteration creates a brand new string and copies all previous characters into it.

The efficient DSA way is:
  1. Append characters or substrings to a LIST (which has O(1) amortized append time).
  2. Use `''.join(list)` at the end (which pre-calculates the size and performs 
     the copy in O(N) linear time).
"""

def demonstrate_performance_gotcha():
    print("\n--- 4.1 String Builder Performance Comparison (N=50,000) ---")
    N = 50000
    
    # O(N^2) Method: Loop Concatenation
    t_start = time_check()
    s = ""
    for i in range(N):
        s += "a"
    t_end = time_check()
    duration_loop = t_end - t_start
    print(f"  Loop Concatenation (s += 'a') time: {duration_loop:.5f} seconds")
    
    # O(N) Method: List Append + Join
    t_start = time_check()
    lst = []
    for i in range(N):
        lst.append("a")
    s_final = "".join(lst)
    t_end = time_check()
    duration_join = t_end - t_start
    print(f"  List Append & ''.join(list) time:   {duration_join:.5f} seconds")
    
    ratio = duration_loop / max(duration_join, 0.00001)
    print(f"  --> Join is approx {ratio:.1f}x faster for N={N}!")

def time_check():
    import time
    return time.perf_counter()


# ================================================================================
# RUNNER
# ================================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("      RUNNING THE PYTHON STRING CORE & PROPERTIES UNDERSTANDING")
    print("=" * 80)

    # Section 1: Memory
    demonstrate_memory_and_interning()
    demonstrate_flexible_representation()
    
    # Section 2: Indexing & Slicing
    demonstrate_indexing()
    demonstrate_slicing()
    
    # Section 3: String Methods
    demonstrate_endswith()
    demonstrate_count()
    demonstrate_find_and_index()
    demonstrate_replace()
    demonstrate_capitalize_and_case()
    
    # Section 4: Performance
    demonstrate_performance_gotcha()
    
    print("\n" + "=" * 80)
    print("                       DEMONSTRATION COMPLETED SUCCESSFULLY")
    print("=" * 80)
