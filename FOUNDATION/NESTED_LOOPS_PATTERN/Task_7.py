# Pattern Task 7 — Alphabet Triangle
# Print:
# A
# AB
# ABC
# ABCD
# Good visualization practice.


n = 4

for i in range(1, n + 1):
    for j in range(1, i + 1):
        # 64 + 1 is 65 ('A'), 64 + 2 is 66 ('B'), and so on
        print(chr(64 + j), end="")
    print()