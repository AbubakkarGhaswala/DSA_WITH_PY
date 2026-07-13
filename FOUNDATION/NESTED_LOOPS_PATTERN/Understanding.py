# =====================================================================
# Hello everyone! Welcome to the world of Nested Loops & Pattern Printing!
# =====================================================================
# This file is your friendly, human-to-human guide to understanding 
# how loops work inside other loops, and how we use them to draw beautiful 
# shapes (patterns) in the terminal.
#
# Let's break it down in the easiest way possible!
# =====================================================================

"""
1. WHAT IS A NESTED LOOP?
-------------------------
In simple terms, a nested loop is just "a loop inside another loop". 

Think of it like a clock:
- The HOUR hand is the OUTER loop.
- The MINUTE hand is the INNER loop.

For every single hour that passes (one step of the outer loop), 
the minute hand must complete a full 60-minute circle (all steps of the inner loop).
Only after the minute hand finishes its full cycle can the hour hand tick forward by one!

Another everyday example is a CALENDAR:
- Outer Loop: WEEKS (e.g., Week 1, Week 2, Week 3...)
- Inner Loop: DAYS of that week (Monday, Tuesday, Wednesday...)

For Week 1 (Outer loop iteration 1):
  - Day 1, Day 2, Day 3, Day 4, Day 5, Day 6, Day 7 (Inner loop runs 7 times)
For Week 2 (Outer loop iteration 2):
  - Day 1, Day 2, Day 3, Day 4, Day 5, Day 6, Day 7 (Inner loop runs 7 times again!)
...and so on!
"""

print("--- ANALOGY: The Calendar Nested Loop ---")
for week in range(1, 3):  # Outer loop: Weeks 1 to 2
    print(f"\n📅 Start of Week {week} (Outer Loop Step {week})")
    
    for day in range(1, 6):  # Inner loop: Workdays Monday to Friday (1 to 5)
        print(f"   -> Day {day} of Week {week} (Inner Loop running)")
        
    print(f"🎉 End of Week {week}!\n" + "-"*40)


"""
2. WHAT IS PATTERN PRINTING?
----------------------------
Pattern printing is a classic way to learn programming logic. It is like digital grid drawing!
Because a terminal prints text line-by-line (from top to bottom, and left to right),
we need two coordinates to draw any 2D shape:
  1. The row number (Vertical position: Y-axis) -> Controlled by the OUTER loop.
  2. The column number (Horizontal position: X-axis) -> Controlled by the INNER loop.

The golden rule of pattern printing is:
- The OUTER loop decides WHICH ROW we are currently printing.
- The INNER loop decides WHAT TO PRINT INSIDE THAT ROW (characters, spaces, stars, numbers).
- Once the inner loop completes a row, we print a new line (jump to the next row).
"""

# Let's see some patterns in action!

# ---------------------------------------------------------
# PATTERN 1: The Solid Square of Stars (e.g., 4 x 4 Grid)
# ---------------------------------------------------------
# Goal: We want to print:
# * * * *
# * * * *
# * * * *
# * * * *
#
# Logic: We have 4 rows (outer loop) and in each row, we print 4 stars (inner loop).

print("\n--- Pattern 1: Solid Square ---")
size = 4
for row in range(size):          # Outer loop: controls rows (0, 1, 2, 3)
    for col in range(size):      # Inner loop: prints stars in columns
        # end=" " keeps the output on the same line with a space
        print("*", end=" ")      
    
    # After finishing the inner loop (a full row of stars), we print an empty line
    # to move our cursor down to the next row.
    print()                      


# ---------------------------------------------------------
# PATTERN 2: The Right-Angled Triangle
# ---------------------------------------------------------
# Goal: We want to print:
# * 
# * * 
# * * * 
# * * * *
#
# Logic: 
# - Row 1 (index 0): We want 1 star
# - Row 2 (index 1): We want 2 stars
# - Row 3 (index 2): We want 3 stars
# - Row 4 (index 3): We want 4 stars
#
# Notice the rule: The number of stars in a row is equal to (row_index + 1).
# Here, the inner loop DEPENDS on the outer loop!

print("\n--- Pattern 2: Right-Angled Triangle ---")
height = 4
for row in range(height):               # Outer loop: row goes from 0 to 3
    # The inner loop runs (row + 1) times.
    # When row is 0, range(1) runs 1 time.
    # When row is 3, range(4) runs 4 times.
    for col in range(row + 1):          
        print("*", end=" ")
        
    print()  # Move to the next row


