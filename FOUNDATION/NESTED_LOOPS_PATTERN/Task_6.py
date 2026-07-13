# Pattern Task 6 — Repeated Number Triangle
# Print:
# 1
# 22
# 333
# 4444
# This pattern teaches:
# row value usage
# repeated printing



n = 4

for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()