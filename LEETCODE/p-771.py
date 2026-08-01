# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

# Example 1:

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:

# Input: jewels = "z", stones = "ZZ"
# Output: 0


jewels = "aA"
stones = "aAAbbbb"


count_similar = 0

for i in jewels:
    for j in stones:
        if i == j:
            count_similar = count_similar + 1

print(count_similar)

