sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

words_count = 0 

for i in sentences:
    split_sen = i.split()
    len_of_sen = len(split_sen)
    if words_count < len_of_sen:
        words_count = len_of_sen

print(words_count)