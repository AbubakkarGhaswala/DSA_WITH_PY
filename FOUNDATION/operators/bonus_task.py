# Hello Everyone and today we are going to solve a problem that we will take student name and 5 marks of student and then we 
# will find the total of all marks , average marks and percentage based on total 


student_name = input("Enter Student Name:- ")
math_marks = int(input(f"Enter The Maths Makrs Of {student_name} :-  "))
science_marks = int(input(f"Enter The Science Marks of {student_name} :- "))
english_marks = int(input(f"Enter The English Marks Od {student_name} :- "))
sports_marks = int(input(f"Enter The Sports Marks Of {student_name} :- "))
programming_marks = int(input(f"Enter The Programming Marks Of {student_name} :- "))

total_marks = math_marks + science_marks + english_marks + sports_marks + programming_marks 

average_marks = total_marks / 5

percentage_based_on_total = total_marks / 500 * 100


print(f"Student Name = {student_name}")
print(f"Obtained Marks Of {student_name} In Maths Out Of 100 Is = {math_marks}")
print(f"Obtained Marks Of {student_name} In Science Out Of 100 Is = {science_marks}")
print(f"Obtained Marks Of {student_name} In English Out Of 100 Is = {english_marks}")
print(f"Obtained Marks Of {student_name} In Sports Out Of 100 Is = {sports_marks}")
print(f"Obtained Marks Of {student_name} In Programming Out Of 100 Is = {programming_marks}")
print(f"Total Obtained Marks Of {student_name} Out Of 500 Is = {total_marks}")
print(f"Average Marks Of {student_name} Out Of 100 Is = {average_marks}")
print(f"Percentage Of {student_name} Based On Total Is = {percentage_based_on_total}")

# Bonus Task Done !