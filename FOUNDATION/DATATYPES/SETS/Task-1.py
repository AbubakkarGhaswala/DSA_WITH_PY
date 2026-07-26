roll_numbers = [101, 102, 103, 101, 102, 104, 105]
print(f"In List :- {roll_numbers}")
print(type(roll_numbers))
Unique_roll_number = set(roll_numbers)
print(f"In Sets :- {Unique_roll_number}")
print(type(Unique_roll_number))


print("")
print("Unique Roll Numbers :- ")
print("")
for i in Unique_roll_number:
    print(f"{i}\n")