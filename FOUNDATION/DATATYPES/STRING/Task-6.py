sentence = "I am learning python programming"

split_sen = sentence.split()

print(split_sen)


largest_word = ""


for i in split_sen:
        if len(i) > len(largest_word):
            largest_word = i


print(largest_word)