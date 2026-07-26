word = "banana"
char = "a"

count_chr = 0


for ch in word:
    if char == ch:
        count_chr = count_chr + 1
    

print(f"{char} found {count_chr} times!!")