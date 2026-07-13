# Pattern Task 3 — Right Triangle
# Print:
# *
# **
# ***
# ****
# Hint mentally:
# stars increase every row



n = 4

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end = " ")
    print()