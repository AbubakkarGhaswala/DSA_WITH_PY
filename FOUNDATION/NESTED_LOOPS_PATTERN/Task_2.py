# Pattern Task 2 — Number Square
# Print:
# 1111
# 2222
# 3333
# 4444
# Observe carefully:
# rows changing
# columns fixed
# VERY important visualization.


n = 4


for i in range(1,n+1):
    for j in range(1,n+1):
        print(i, end = " ")
    print()