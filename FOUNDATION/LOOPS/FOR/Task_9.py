# Hello Everyone !!
# Task 9 :- Take Input String From User And count Voweks In It!!

user_input = input("Please Enter Your Name: ")
count = 0

for i in user_input:
    if i in 'AEIOUaeiou':
        count = count + 1
        print(f"Vowel Found:- {i}")
    
print(f"Total Vowels: {count}")