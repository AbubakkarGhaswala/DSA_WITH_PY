word = "Hello"

rev_word = ""

for ch in range(len(word)-1,-1,-1):
    rev_word = rev_word + word[ch]

if word == rev_word:
    print("It's Palindrome!!")
else :
    print("It's Not Palindrome!!")