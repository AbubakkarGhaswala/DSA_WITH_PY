numbers = [1,2,2,3,4,4,5]

new_number = []


for i in numbers:
    if i not in new_number:
        new_number.append(i)

   
print(new_number)