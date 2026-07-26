# Hello Everyone !
# So our task 3 is about finding max number in list without using max function

data = [15,8,90,23,45]

maxx = data[0]


for i in data:
    if i > maxx:
        maxx = i

print(maxx)