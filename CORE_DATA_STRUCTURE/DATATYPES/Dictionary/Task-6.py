word = "banana"

counter_dic = {}

for i in word:
    if i in counter_dic:
        counter_dic.update({i:counter_dic[i] + 1})
    else :
        counter_dic[i] = 1

print(counter_dic)
