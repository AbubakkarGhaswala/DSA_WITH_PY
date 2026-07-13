# Pattern Task 5 — Number Triangle
# Print:
# 1
# 12
# 123
# 1234
# VERY important for nested-loop understanding.



n = 4

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end = " ")
    print()