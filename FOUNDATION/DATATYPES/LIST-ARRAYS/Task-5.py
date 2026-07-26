# Hello Everyone !
# Our Task 5 is to count even number and odd numbers are in a list


numbers = [1,2,3,4,5,6,7,8]

even_count = 0

odd_count = 0

for i in numbers:
    if i % 2 == 0:
        even_count = even_count + 1
    elif i % 2 != 0:
        odd_count = odd_count + 1


print(f"Even Count = {even_count}")
print(" ")
print(f"Odd Count = {odd_count}")