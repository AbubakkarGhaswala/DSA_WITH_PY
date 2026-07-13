# Hello Everyone and welcome today we are going to learn about the Conditional Logics


# ==============================================


# what is the meaning of conditional statement? 
# - So simple words conditional statement is a way to make a decision in a program
# - For Example if i say that "if it is raining outside then i will not go outside"



# So here is the structure of the conditional statement in code 


# if (condition) : 

is_rain = True

if (is_rain) : 
    print("I will not go outside")
else : 
    print("I am outside")



# So Here if (is_rain) is True then it will print "I will not go outside" 
# else it will print "I am outside"

# and we have also another keyword if we have more than two conditions 
# that is elif 
# example if i say that "if it is raining outside then i will not go outside" 
# else if it is sunny outside then i will go outside" 
# else i will go outside" 

# and we can also add if we have more than two conditions 

is_rain = True
is_sunny = False
is_cloudy = True

if (is_rain) :
    print("I will not go outside")
elif (is_sunny) :
    print("I will go outside")
else :
    print("I am outside")

# And now let's try to change the values of is_rain, is_sunny and is_cloudy 

# if is_rain is True and is_sunny is True then it will print "I will not go outside" 
# else if is_rain is True and is_sunny is False then it will print "I will not go outside" 
# else if is_rain is False and is_sunny is True then it will print "I will go outside" 
# else it will print "I am outside" 

# So this is what conditional statement is and it is very useful in programming 

# Now let's talk about the nested if statement 

# Nested if statement is a if statement inside another if statement 
# example 

if (is_rain) : 
    print("I will not go outside")
    if (is_sunny) : 
        print("I will go outside")
    else : 
        print("I am outside")
else : 
    print("I am outside")

# So heres the nested if also so all done and now lets do some tasks in another files ! Thank you.