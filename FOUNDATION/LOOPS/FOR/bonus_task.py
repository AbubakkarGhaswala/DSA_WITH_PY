# Bonus Task — Mini Student Result System
# BEFORE patterns.
# Because this task combines almost EVERYTHING you learned till now:
# variables
# input
# arithmetic
# conditions
# loops
# totals
# averages
# logical decision-making
# It’s actually a very good “checkpoint project.”
# Requirements (Clear Version)
# Step 1
# Take:
# student name
# 5 subject marks
# Step 2
# Calculate:
# total marks
# average
# percentage
# Step 3
# Assign Grade
# Example logic idea:
# 90+ → A+
# 80+ → A
# 70+ → B
# 60+ → C
# below 40 → Fail
# You can design grading yourself too.
# Step 4
# Display Proper Result Card
# Example style:
# student name
# total
# percentage
# grade
# pass/fail status
# Make it clean.
# IMPORTANT EDGE CASES
# Think about:
# marks below 0
# marks above 100
# decimal marks
# failed subjects
# This is where logic improves.
# BONUS FEATURES (Optional)
# If you want stronger practice:
# count failed subjects
# highest marks
# lowest marks
# distinction message
# percentage formatting


# Student Details :- 


stu_name = input("Please Enter Student Name :- ")
stu_roll_no = int(input(f"Please Enter {stu_name}'s Roll Number :- "))

# Input Of 5 Subject Marks (Math,Science,English,Computer,Physics)

while True :
    math_marks = int(input(f"Please Enter {stu_name}'s Math Marks :- "))

    if math_marks < 0 or math_marks > 100:
        print("Please Enter Valid Marks between 0 to 100")
    else :
        math_marks = math_marks
        break

while True :
    science_marks = int(input(f"Please Enter {stu_name}'s Science Marks :- "))

    if science_marks < 0 or science_marks > 100:
        print("Please Enter Valid Marks between 0 to 100")
    else :
        science_marks = science_marks
        break

while True :
    English_marks = int(input(f"Please Enter {stu_name}'s English Marks :- "))

    if English_marks < 0 or English_marks > 100:
        print("Please Enter Valid Marks between 0 to 100")
    else :
        English_marks = English_marks
        break

while True :
    computer_marks = int(input(f"Please Enter {stu_name}'s Computer Marks :- "))

    if computer_marks < 0 or computer_marks > 100:
        print("Please Enter Valid Marks between 0 to 100")
    else :
        computer_marks = computer_marks
        break

while True :
    physics_marks = int(input(f"Please Enter {stu_name}'s Physics Marks :- "))

    if physics_marks < 0 or physics_marks > 100:
        print("Please Enter Valid Marks between 0 to 100")
    else :
        physics_marks = physics_marks
        break

# Calculate Total Marks
total_marks = math_marks + science_marks + English_marks + computer_marks + physics_marks

# Calculate Average Marks 
average_marks = total_marks / 5

# Calculate Percentage 
percentage_based_on_total = (total_marks / 500) * 100


# Assign Grade Variable For Each Subject 

math_grade = ""
science_grade = ""
English_grade = ""
computer_grade = ""
physics_grade = ""

# Grade For Maths Subject
if math_marks >= 90:
    math_grade = "A+"
elif math_marks >= 80:
    math_grade = "A"
elif math_marks >= 70:
    math_grade = "B"
elif math_marks >= 60:
    math_grade = "C"
elif math_marks >= 50:
    math_grade = "D"
else:
    math_grade = "F"


# Grade For Science Subject
if science_marks >= 90:
    science_grade = "A+"
elif science_marks >= 80:
    science_grade = "A"
elif science_marks >= 70:
    science_grade = "B"
elif science_marks >= 60:
    science_grade = "C"
elif science_marks >= 50:
    science_grade = "D"
else:
    science_grade = "F"


# Grade For English Subject
if English_marks >= 90:
    English_grade = "A+"
elif English_marks >= 80:
    English_grade = "A"
elif English_marks >= 70:
    English_grade = "B"
elif English_marks >= 60:
    English_grade = "C"
elif English_marks >= 50:
    English_grade = "D"
else:
    English_grade = "F"


# Grade For Computer Subject
if computer_marks >= 90:
    computer_grade = "A+"
elif computer_marks >= 80:
    computer_grade = "A"
elif computer_marks >= 70:
    computer_grade = "B"
elif computer_marks >= 60:
    computer_grade = "C"
elif computer_marks >= 50:
    computer_grade = "D"
else:
    computer_grade = "F"


# Grade For Physics Subject
if physics_marks >= 90:
    physics_grade = "A+"
elif physics_marks >= 80:
    physics_grade = "A"
elif physics_marks >= 70:
    physics_grade = "B"
elif physics_marks >= 60:
    physics_grade = "C"
elif physics_marks >= 50:
    physics_grade = "D"
else:
    physics_grade = "F"


# OverAll Grade variable
overall_grade = ""

if percentage_based_on_total >= 90:
    overall_grade = "A+"
elif percentage_based_on_total >= 80:
    overall_grade = "A"
elif percentage_based_on_total >= 70:
    overall_grade = "B"
elif percentage_based_on_total >= 60:
    overall_grade = "C"
elif percentage_based_on_total >= 50:
    overall_grade = "D"
else:
    overall_grade = "F"


# Bonus features & overall pass/fail status calculations using loop (For Loop Practice)
subjects = ["Math", "Science", "English", "Computer", "Physics"]
marks_list = [math_marks, science_marks, English_marks, computer_marks, physics_marks]
grades_list = [math_grade, science_grade, English_grade, computer_grade, physics_grade]

failed_subjects_count = 0
highest_marks = -1
highest_subject = ""
lowest_marks = 101
lowest_subject = ""

for i in range(len(subjects)):
    current_subject = subjects[i]
    current_mark = marks_list[i]
    
    # Count failed subjects
    if current_mark < 40:
        failed_subjects_count += 1
        
    # Find highest marks
    if current_mark > highest_marks:
        highest_marks = current_mark
        highest_subject = current_subject
        
    # Find lowest marks
    if current_mark < lowest_marks:
        lowest_marks = current_mark
        lowest_subject = current_subject

# Update overall grade and pass status based on fail condition for individual subjects
if failed_subjects_count > 0:
    overall_grade = "Fail"
    pass_fail_status = "FAIL"
else:
    pass_fail_status = "PASS"

# Distinction check (Only if student has passed all subjects and percentage >= 90)
has_distinction = percentage_based_on_total >= 90 and pass_fail_status == "PASS"


# --- PRINT THE RESULT CARD ---
print("\n" + "=" * 55)
print(f"{'STUDENT RESULT CARD':^55}")
print("=" * 55)
print(f" Student Name : {stu_name:<20} Roll No : {stu_roll_no:<10}")
print("-" * 55)
print(f" {'SUBJECT':<15} | {'MARKS':<10} | {'GRADE':<10} | {'STATUS':<10}")
print("-" * 55)

for i in range(len(subjects)):
    sub_status = "Pass" if marks_list[i] >= 40 else "Fail"
    print(f" {subjects[i]:<15} | {marks_list[i]:<10} | {grades_list[i]:<10} | {sub_status:<10}")
    
print("-" * 55)
print(f" {'Total Marks':<15} : {total_marks} / 500")
print(f" {'Average Marks':<15} : {average_marks:.2f}")
print(f" {'Percentage':<15} : {percentage_based_on_total:.2f}%")
print(f" {'Overall Grade':<15} : {overall_grade}")

if pass_fail_status == "PASS":
    print(f" {'Final Status':<15} : \033[1;32mPASS\033[0m")
else:
    print(f" {'Final Status':<15} : \033[1;31mFAIL\033[0m")
    
print("=" * 55)

# Print Bonus Features Summary
print(f"{'ADDITIONAL METRICS (BONUS FEATURES)':^55}")
print("-" * 55)
print(f" Highest Scoring Subject : {highest_subject} ({highest_marks})")
print(f" Lowest Scoring Subject  : {lowest_subject} ({lowest_marks})")
print(f" Failed Subjects Count   : {failed_subjects_count}")

if has_distinction:
    print("\n" + "*" * 55)
    print(f"\033[1;33m🏆 Congratulations {stu_name}! You achieved DISTINCTION! 🏆\033[0m")
    print("*" * 55)
print("=" * 55 + "\n")



