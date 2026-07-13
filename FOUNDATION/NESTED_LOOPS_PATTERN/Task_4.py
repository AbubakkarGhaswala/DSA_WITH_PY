# Pattern Task 4 — Reverse Triangle
# Print:
# ****
# ***
# **
# *
# Now opposite thinking:
# stars decrease every row


n = 4

for i in range(n , 0 , -1):
    for j in range(i):
        print("*", end = " ")
    print()
