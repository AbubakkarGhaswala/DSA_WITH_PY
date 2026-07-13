# Hello everyone our task 4 is about to make a number guessing game using while 
# first we will store one secret number in one variable and second variable we will ask for input 
# it will ask again and again untill user guess the correct number


secret_number = 17

while True:
    guess_input = int(input("Guess The Corrcet Number :- "))
    if guess_input == secret_number:
        print(f"Yayy 🤩🥳 !! You've Guess Correct Number {guess_input} And Secret Number Is {secret_number}")
        break

    else :
        print("Ohho ! Wrong Guess Keep Trying ! Good Luck!! 🤞 ")
    
print("Loop End")