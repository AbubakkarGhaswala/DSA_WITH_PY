# So In this file we are going to understand types of operators and what they actually do in code !

# so there. are 7 types of operators:
# 1. Arithmetic operators (+, -, *, /, %, //, **)
# 2. Comparison operators ( ==, !=, >, <, >=, <= )
# 3. Assignment operators ( =, +=, -=, *=, /=, %=, **= )
# 4. Logical operators ( and, or, not )
# 5. Identity operators ( is, is not )
# 6. Membership operators ( in, not in )
# 7. Bitwise operators ( &, |, ^, ~, <<, >> )

# so our first type of operator is Arithmetic operators (+, -, *, /, %, //, **)

# + (Addition):  it will do addition of two numbers which are assign to "a" and "b"
a = 5 
b = 10 
c = a + b 
print(c)

# - (Subtraction): it will do subtraction of two numbers which are assign to "a" and "b" 
a = 5 
b = 10 
c = a - b 
print(c)

# * (Multiplication):  it will do multiplication of two numbers which are assign to "a" and "b" 
a = 5 
b = 10 
c = a * b 
print(c)

# / (Division): it will do division of two numbers which are assign to "a" and "b" 
a = 5 
b = 10 
c = a / b 
print(c)

# % (Modulo): it will help us to find the reminder of the division of two numbers like 5/2 so 2 * 2 = 4 and 5 - 4 = 1 so 1 will be the reminder 
a = 5 
b = 10 
c = a % b 
print(c)


# ** (Exponentiation): it will help us to find the power of the number like 5/10 so 10 to the power of 5
a = 5 
b = 10 
c = a ** b 
print(c)
 
# // (Floor Division): it will help us to find the quotient of the division of two numbers like 5/2 so 2*2=4 so our reminder will 1 cause of 5/2 = 2 and will be the quotient 
a = 5 
b = 10 
c = a // b 
print(c)

# so our second type of operator is Comparison operators ( ==, !=, >, <, >=, <= )

# == (Equality): it will check if the two numbers are equal or not 
a = 5 
b = 10 
print(a == b)

# != (Not Equality): it will check if the two numbers are not equal or not 
a = 5 
b = 10 
print(a != b)

# > (Greater Than): it will check if the first number is greater than the second number 
a = 5 
b = 10 
print(a > b)

# < (Less Than): it will check if the first number is less than the second number 
a = 5 
b = 10 
print(a < b)

# >= (Greater Than or Equal To): it will check if the first number is greater than or equal to the second number 
a = 5 
b = 10 
print(a >= b)

# <= (Less Than or Equal To): it will check if the first number is less than or equal to the second number 
a = 5 
b = 10 
print(a <= b)



# So Our third operators is Logical operators ( and, or, not )

# and (AND): it will check if both the conditions are true or not 
a = 5 
b = 10 
print(a and b)

# or (OR): it will check if any of the conditions are true or not 
a = 5 
b = 10 
print(a or b)

# not (NOT): it will reverse the condition 
a = 5 
b = 10 
print(not a)

# so our 4th type of operator is Assignment operators ( =, +=, -=, *=, /=, %=, **= )

# = (Assignment): it will assign the value of the right side to the left side 
a = 5 
b = 10 
a = b 
print(a)

# += (Addition Assignment): it will add the value of the right side to the left side and assign the result to the left side 
a = 5 
b = 10 
a += b 
print(a)

# -= (Subtraction Assignment): it will subtract the value of the right side from the left side and assign the result to the left side 
a = 5 
b = 10 
a -= b 
print(a)

# *= (Multiplication Assignment): it will multiply the value of the right side with the left side and assign the result to the left side 
a = 5 
b = 10 
a *= b 
print(a)

# /= (Division Assignment): it will divide the value of the right side from the left side and assign the result to the left side 
a = 5 
b = 10 
a /= b 
print(a)

# %= (Modulo Assignment): it will find the reminder of the division of the right side from the left side and assign the result to the left side 
a = 5 
b = 10 
a %= b 
print(a)

# **= (Exponentiation Assignment): it will find the power of the right side from the left side and assign the result to the left side 
a = 5 
b = 10 
a **= b 
print(a)

# so our 5th type of operator is Identity operators ( is, is not )

# is (Identity): it will check if the two numbers are same or not 
a = 5 
b = 10 
print(a is b)

# is not (Not Identity): it will check if the two numbers are not same or not 
a = 5 
b = 10 
print(a is not b)


# so our 6th type of operator is Bitwise operators ( &, |, ^, ~, <<, >> )

# & (Bitwise AND): it will perform bitwise AND operation on the two numbers 
a = 5 
b = 10 
print(a & b)

# | (Bitwise OR): it will perform bitwise OR operation on the two numbers 
a = 5 
b = 10 
print(a | b)

# ^ (Bitwise XOR): it will perform bitwise XOR operation on the two numbers 
a = 5 
b = 10 
print(a ^ b)

# ~ (Bitwise NOT): it will perform bitwise NOT operation on the two numbers 
a = 5 
b = 10 
print(~a)

# << (Bitwise Left Shift): it will perform bitwise left shift operation on the two numbers 
a = 5 
b = 10 
print(a << b)

# >> (Bitwise Right Shift): it will perform bitwise right shift operation on the two numbers 
a = 5 
b = 10 
print(a >> b)


# How to find the binary number ?
# we have a number 10 okat now if we want to find the binary so for find the binary we hacve binary num = 2 now we will do 
# divide 10 by 2 so we get quotient = 5 and reminder = 0 
# then divide 5 by 2 so we get quotient = 2 and reminder = 1 
# then divide 2 by 2 so we get quotient = 1 and reminder = 0 
# then divide 1 by 2 so we get quotient = 0 and reminder = 1 
# now we will write the reminder in reverse order so we get 1010 so this is the binary of 10 

# and when we have binaey number 0,0 = 0, if we have 0,1 = 1, if we have 1,0 = 0, if we have 1,1 = 1 this is just for AND operator 
# and when we have binary number 0|0 = 0, 0|1 = 1, 1|0 = 1, 1|1 = 1 this is just for OR operator 
# and when we have binary number 0^0 = 0, 0^1 = 1, 1^0 = 1, 1^1 = 0 this is just for XOR operator 


# so our 7th type of operator is Membership operators ( in, not in )


a = [1, 2, 3, 4, 5] 
b = 3 

print(b in a) # it will check if b is in a

print(b not in a) # it will check if b is not in a
