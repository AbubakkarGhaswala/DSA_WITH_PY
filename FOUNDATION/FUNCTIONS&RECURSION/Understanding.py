"""
================================================================================
MASTERING FUNCTIONS & RECURSION IN PYTHON
================================================================================
A deep-dive conceptual guide, code laboratory, and edge-case reference.
Designed to go beyond basic tutorials and explore Python's execution model, 
stack frames, memory overhead, scoping rules, and recursion patterns.

Written for: Deep DSA Understanding (Python 3.x)
================================================================================
"""

import sys
import functools
import time
from typing import List, Dict, Any, Callable

# ================================================================================
# SECTION 1: THE PYTHON FUNCTION EXECUTION MODEL & ADVANCED ARGUMENTS
# ================================================================================

"""
--- 1.1 Memory Model: Pass-by-Object-Reference ---
Python doesn't use traditional 'pass-by-value' or 'pass-by-reference'. It uses 
'pass-by-object-reference' (sometimes called 'pass-by-assignment').

When you pass an argument to a function:
  - You pass a copy of the *reference* to the object.
  - If the object is IMMUTABLE (int, float, str, tuple, frozenset):
    Modifying it inside the function creates a new object. The original remains unchanged.
  - If the object is MUTABLE (list, dict, set, custom classes):
    Modifying it in-place inside the function affects the caller's object because 
    both variables point to the exact same memory address.
"""

def demonstrate_pass_by_reference():
    print("\n--- 1.1 Pass-By-Object-Reference Demo ---")
    
    def modify_values(x_val: int, list_val: List[int]):
        print(f"  Inside (Initial): x_val ID = {id(x_val)}, list_val ID = {id(list_val)}")
        x_val += 10          # Creates a new int object because ints are immutable
        list_val.append(99)  # Mutates the existing list object in place
        print(f"  Inside (Modified): x_val ID = {id(x_val)} (CHANGED), list_val ID = {id(list_val)} (SAME)")

    a = 5
    b = [1, 2, 3]
    print(f"Before call: a = {a} (ID: {id(a)}), b = {b} (ID: {id(b)})")
    modify_values(a, b)
    print(f"After call:  a = {a} (still 5), b = {b} (mutated!)")


"""
--- 1.2 The Mutable Default Argument Trap ---
Default arguments in Python are evaluated ONLY ONCE, when the function is defined, 
not every time the function is called.
If you use a mutable object (like a list or dict) as a default parameter, that same 
object is shared across all function invocations!
"""

def mutable_default_trap(item: Any, container: List[Any] = []): # <-- The trap!
    container.append(item)
    return container

def mutable_default_correct(item: Any, container: List[Any] = None):
    # The industry standard fix:
    if container is None:
        container = []
    container.append(item)
    return container

def demonstrate_mutable_defaults():
    print("\n--- 1.2 Mutable Default Arguments Demo ---")
    print("Trap calls (sharing the same list object):")
    print(f"  Call 1: {mutable_default_trap('A')}")
    print(f"  Call 2: {mutable_default_trap('B')}")  # Notice 'A' is still there!
    
    print("Correct calls (fresh list created if None):")
    print(f"  Call 1: {mutable_default_correct('A')}")
    print(f"  Call 2: {mutable_default_correct('B')}")  # Clean!


"""
--- 1.3 Variable Scope & The LEGB Rule ---
Python resolves variable names using the LEGB hierarchy:
  1. Local (L): Inside the current function.
  2. Enclosing (E): Inside any enclosing / nested functions.
  3. Global (G): Module-level variables defined at the top file level.
  4. Built-in (B): Names pre-loaded by Python (like len, range, print).

To modify a Global or Enclosing variable from a narrower scope, you must use 
the 'global' or 'nonlocal' keywords. Without them, Python assumes you are creating 
a new local variable.
"""

# Global variable
counter = 0

def demonstrate_scopes():
    print("\n--- 1.3 Scoping (LEGB) & Modifiers Demo ---")
    
    # 1. Modifying a global variable
    def increment_global():
        global counter
        counter += 1
    
    # 2. Modifying an enclosing variable (Closures)
    def outer_function():
        enclosing_var = "Original Outer"
        
        def inner_function():
            nonlocal enclosing_var
            enclosing_var = "Modified by Inner"
            
        print(f"  Before inner call: enclosing_var = '{enclosing_var}'")
        inner_function()
        print(f"  After inner call:  enclosing_var = '{enclosing_var}'")

    increment_global()
    print(f"Global counter modified: {counter}")
    outer_function()


"""
--- 1.4 Variadic Arguments (*args, **kwargs) ---
*args collects extra positional arguments into a TUPLE.
**kwargs collects extra keyword arguments into a DICTIONARY.
This is critical for writing decorators, wrappers, and APIs where argument 
signatures are dynamic or determined at runtime.
"""

def print_params(title: str, *args, **kwargs):
    print(f"\n--- 1.4 Variadic Args: {title} ---")
    print(f"  args (type {type(args)}): {args}")
    print(f"  kwargs (type {type(kwargs)}): {kwargs}")


# ================================================================================
# SECTION 2: DEEP DIVE INTO RECURSION & CALL STACKS
# ================================================================================

"""
--- 2.1 The Philosophy of Recursion ---
Recursion is a programming technique where a function solves a problem by calling 
itself on smaller instances of the same problem.

Every valid recursive function must have two components:
  1. Base Case: The condition under which the function stops calling itself. 
     Without this, you get infinite recursion (resulting in a RecursionError).
  2. Recursive Case (Reduction Step): The logic that breaks the problem into 
     smaller sub-problems and moves the state closer to the base case.

--- 2.2 Stack Frames & Execution Stack ---
When a function is called, Python allocates a block of memory called a "Stack Frame" 
on the call stack. This frame stores:
  - Local variables
  - Parameters passed to the function
  - The return address (where to resume execution after returning)

In recursion, each nested call pushes a NEW stack frame onto the call stack. 
Only when a base case is hit do these frames start resolving and getting popped off.
"""

def visualize_factorial_stack(n: int, depth: int = 0) -> int:
    """
    Computes factorial but prints call-stack visualizations.
    """
    indent = "    " * depth
    print(f"{indent}--> Call visualize_factorial_stack(n={n}) [Stack Frame created]")
    
    # Base Case
    if n <= 1:
        print(f"{indent}<-- Reached Base Case (n={n}). Returning 1. [Frame popping]")
        return 1
    
    # Recursive Case
    result = n * visualize_factorial_stack(n - 1, depth + 1)
    
    print(f"{indent}<-- Returning {result} for n={n}. [Frame popping]")
    return result


"""
--- 2.3 Head Recursion vs. Tail Recursion ---
- Head Recursion: The recursive call is made at the beginning of the function (or before 
  other processing). The computations are performed on the return journey (after the recursive 
  call resolves).
- Tail Recursion: The recursive call is the ABSOLUTE LAST operation of the function. No 
  computations are left to do after the recursive call returns.
  
*Python Specifics*: Python does NOT support Tail Call Optimization (TCO). In languages like 
Haskell, Scala, or Scheme, tail-recursive functions are optimized into simple loops under the 
hood, avoiding stack frame build-up. In Python, even tail-recursive functions will consume O(N) 
stack space and trigger Stack Overflow (RecursionError) for large inputs.
"""

# Head Recursion: Needs to wait for the next call to finish to perform the multiplication.
def head_recursive_factorial(n: int) -> int:
    if n <= 1:
        return 1
    sub_problem = head_recursive_factorial(n - 1)  # Recursion is at the "head" / middle
    return n * sub_problem                        # Operations performed on return

# Tail Recursion: The call is the last thing executed.
def tail_recursive_factorial(n: int, accumulator: int = 1) -> int:
    if n <= 1:
        return accumulator
    # The last action is strictly the recursive call itself, passing state forward.
    return tail_recursive_factorial(n - 1, n * accumulator)


"""
--- 2.4 Tree Recursion ---
A function is tree-recursive when it makes MULTIPLE recursive calls in a single execution path.
This produces a branching tree of calls. 
Classic example: The Fibonacci sequence.
Complexity: Standard recursive Fibonacci is highly inefficient because it recomputes the 
same sub-problems repeatedly. Its time complexity is exponential: O(2^n).

Visual representation of fibonacci(4):
                      fib(4)
                     /      \\
                fib(3)      fib(2)
                /    \\       /    \\
            fib(2)  fib(1) fib(1) fib(0)
            /    \\
        fib(1)  fib(0)
"""

def tree_recursive_fibonacci(n: int, stats: Dict[str, int]) -> int:
    stats['calls'] += 1
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return tree_recursive_fibonacci(n - 1, stats) + tree_recursive_fibonacci(n - 2, stats)


# ================================================================================
# SECTION 3: MITIGATING RECURSION OVERHEAD & OPTIMIZATIONS
# ================================================================================

"""
--- 3.1 Memoization (Dynamic Programming) ---
To solve the exponential time complexity of tree recursion, we cache the results 
of expensive function calls.
We can implement this manually using a dictionary, or use Python's built-in 
`functools.lru_cache` decorator.
"""

# Manual Memoization
memo_cache = {}
def fibonacci_memoized(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n not in memo_cache:
        memo_cache[n] = fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)
    return memo_cache[n]

# Auto Memoization using Python's LRU (Least Recently Used) cache
@functools.lru_cache(maxsize=None)
def fibonacci_lru(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)


"""
--- 3.2 Simulating Recursion with an Explicit Stack ---
Any recursive function can be rewritten iteratively using a loop and a stack data structure 
(usually a Python list). This completely bypasses Python's system stack limit, allowing 
you to process deeply nested data structures safely without memory limit crashes.
"""

def iterative_factorial(n: int) -> int:
    """
    Computes factorial using an explicit stack simulation.
    Crucial design pattern for production-grade graph/tree traversals.
    """
    stack = []
    # We push a tuple onto the stack: (state_identifier, arguments, local_variables)
    # States: 
    #   0: Initial/Entry state
    #   1: Return/Aggregation state
    
    stack.append(('entry', n, None))
    result_val = 1
    
    while stack:
        state, val, ret = stack.pop()
        
        if state == 'entry':
            if val <= 1:
                # Base case equivalent
                result_val = 1
            else:
                # Save execution state to resume later, and push the next recursive call
                stack.append(('return', val, None))
                stack.append(('entry', val - 1, None))
                
        elif state == 'return':
            # Aggregation step: multiply our current val with what the sub-call computed
            result_val = val * result_val
            
    return result_val


# ================================================================================
# SECTION 4: EDGE CASES, ERROR HANDLING & ADVANCED TOPICS
# ================================================================================

"""
--- 4.1 The Recursion Limit & Python Safety Nets ---
By default, Python sets a limit on the maximum recursion depth (usually around 1000). 
This prevents an out-of-control recursive function from completely consuming 
system memory and crashing the OS process (Segfault).
"""

def demonstrate_recursion_limit():
    print("\n--- 4.1 Recursion Limit & Error Catching ---")
    print(f"Current System Recursion Limit: {sys.getrecursionlimit()}")
    
    def infinite_recursion(depth=1):
        try:
            infinite_recursion(depth + 1)
        except RecursionError as e:
            # We catch it on the first frame that receives the exception
            print(f"  [CRASH DETECTED] Caught RecursionError at depth: {depth}!")
            print(f"  Error Message: {e}")
            return
            
    infinite_recursion()

    # Dynamic Adjustments:
    # Python allows setting a higher limit via sys.setrecursionlimit().
    # WARNING: Increasing this too high can cause a hard crash (segfault) of the Python
    # interpreter if the C stack memory limit of the operating system is breached.
    print("  Temporarily raising recursion limit to 2000...")
    original_limit = sys.getrecursionlimit()
    try:
        sys.setrecursionlimit(2000)
        # Deep recursive operation...
    finally:
        sys.setrecursionlimit(original_limit)  # Always restore system settings!


"""
--- 4.2 Non-Integer & Negative Inputs ---
A classic recursive bug is not verifying inputs. 
For instance, what happens to factorial(5.5) or factorial(-1)?
  - factorial(-1) will run forever, decrementing to -2, -3, ... until RecursionError.
  - factorial(5.5) will skip the `n == 1` condition (e.g., 5.5 -> 4.5 -> 3.5 -> ... -> 0.5 -> -0.5) 
    and also recurse infinitely.

--- Defensive Design Rules: ---
1. Validate inputs (type checking & range constraints).
2. Use inequalities (e.g., `n <= 1`) rather than exact equality (`n == 1`) in base cases.
"""

def robust_factorial(n: int) -> int:
    # Defensive validations:
    if not isinstance(n, int):
        raise TypeError("Factorial is only defined for integers.")
    if n < 0:
        raise ValueError("Factorial is undefined for negative integers.")
        
    # Using inequality <= instead of == for robustness
    if n <= 1:
        return 1
    return n * robust_factorial(n - 1)


"""
--- 4.3 State Mutability in Recursive Backtracking ---
When solving combinatorial algorithms (permutations, subsets, sudoku solver, N-queens):
  - If you pass a list representing the path/current solution, modifications are shared.
  - If you do not copy the state when storing it or when recursing, you will end up with 
    incorrect or empty results because elements are popped off during backtracking.
"""

def generate_subsets(nums: List[int]) -> List[List[int]]:
    """
    Classic backtracking recursion to generate all subsets.
    Demonstrates state copying edge-cases.
    """
    results = []
    
    def backtrack(start_index: int, current_subset: List[int]):
        # Edge case / Gotcha: We MUST make a copy of current_subset (using list() or .copy())
        # If we append current_subset directly, subsequent mutations will ruin the archived result!
        results.append(list(current_subset)) 
        
        for i in range(start_index, len(nums)):
            current_subset.append(nums[i])      # Choose
            backtrack(i + 1, current_subset)    # Explore
            current_subset.pop()                # Unchoose (Backtrack)
            
    backtrack(0, [])
    return results


# ================================================================================
# SECTION 5: DEMONSTRATION & RUNNER
# ================================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("      RUNNING THE FUNCTIONS AND RECURSION CONCEPT LABORATORY")
    print("=" * 80)

    # 1. Parameter Passing
    demonstrate_pass_by_reference()
    
    # 2. Default Mutable Arguments
    demonstrate_mutable_defaults()
    
    # 3. Variable Scope and LEGB Rule
    demonstrate_scopes()
    
    # 4. Variadic Arguments
    print_params("Calling with positionals and keyword arguments", 10, 20, "banana", x=1, y=2)
    
    # 5. Visualizing Stack Frames
    print("\n--- 2.2 Stack Frame Visualization (Factorial 4) ---")
    visualize_factorial_stack(4)
    
    # 6. Comparing Head vs Tail Recursion
    print("\n--- 2.3 Head vs Tail Recursion Evaluation ---")
    print(f"  Head recursion result (5!): {head_recursive_factorial(5)}")
    print(f"  Tail recursion result (5!): {tail_recursive_factorial(5)}")
    
    # 7. Exponential Complexity of Tree Recursion
    print("\n--- 2.4 Tree Recursion Overhead (Naive vs Caching) ---")
    stats = {'calls': 0}
    t_start = time.perf_counter()
    naive_res = tree_recursive_fibonacci(30, stats)
    t_end = time.perf_counter()
    print(f"  Naive Fibonacci(30) = {naive_res}")
    print(f"  Total recursive function calls: {stats['calls']:,}")
    print(f"  Time taken: {t_end - t_start:.4f} seconds")
    
    # Cached / Memoized comparison
    t_start = time.perf_counter()
    memo_res = fibonacci_lru(30)
    t_end = time.perf_counter()
    print(f"  LRU Cached Fibonacci(30) = {memo_res}")
    print(f"  Time taken with memoization: {t_end - t_start:.6f} seconds (Extremely Fast!)")
    
    # 8. Explicit Stack Simulation
    print("\n--- 3.2 Explicit Stack Simulation ---")
    iter_fact = iterative_factorial(5)
    print(f"  Iterative Factorial (5!): {iter_fact}")
    
    # 9. Recursion Limits
    demonstrate_recursion_limit()
    
    # 10. Robust Defensive Design
    print("\n--- 4.2 Robust Exception Checking ---")
    try:
        robust_factorial(-5)
    except ValueError as e:
        print(f"  Caught expected error: {e}")
        
    # 11. Mutability and Backtracking
    print("\n--- 4.3 Backtracking Subset Generation ---")
    test_nums = [1, 2, 3]
    subsets = generate_subsets(test_nums)
    print(f"  All subsets of {test_nums}: {subsets}")
    
    print("\n" + "=" * 80)
    print("                       DEMONSTRATION COMPLETED SUCCESSFULLY")
    print("=" * 80)
