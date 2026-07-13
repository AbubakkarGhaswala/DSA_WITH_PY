# Hello Everyone!
# So our task 4 is about finding minimum number in list without using min function

data = [15,8,90,23,45]

minn = data[0]


for i in data:
    if i < minn:
        minn = i

print(minn)