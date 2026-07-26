dev_a = {
    "Python",
    "SQL",
    "Git",
    "Docker",
    "Linux"
}

dev_b = {
    "Python",
    "Java",
    "Git",
    "AWS",
    "Docker"
}


# Question 1

# Print all technologies that both developers know.



tech_both = dev_a & dev_b

print(f"The Technologies Both Dev Know :- {tech_both}")


# Question 2

# Print technologies only Developer A knows.

tech_only_a = dev_a - dev_b
print(f"The Technologies Only Dev A Known :- {tech_only_a}")


# Question 3

# Print technologies only Developer B knows.

tech_only_b = dev_b - dev_a
print(f"The Technologies Only Dev B Known :- {tech_only_b}")



# Question 4

# Print all unique technologies known by both developers.

unique_tech = dev_a | dev_b
print(f"The Technologies That Are Unique Known By Both Dev :- {unique_tech}")


# Question 5

# Print the total number of unique technologies.

total_num_of_unique_tech = len(unique_tech)
print(f"Total Unique Technologies :- {total_num_of_unique_tech}")


# Question 6

# Print whether Developer A knows every technology that Developer B knows.

print(f"Developer A Tech:- {dev_a}")
print("")
print(f"Developer B Tech:- {dev_b}")

if dev_a.issuperset(dev_b) == True:
    print("Yes - Developer A Knows Every Techonlogy That Developer B Knows!!")
else :
    print("No - Developer A Does Not Knows Every Techonlogy That Developer B Knows!!")


# Question 7 (Bonus)

# Print whether both developers know exactly the same technologies.

if dev_a == dev_b:
    print("Yes, both have identical skills.")
else:
    print("No, their skill sets are different.")