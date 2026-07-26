registered_students = {
    "Abu",
    "Ali",
    "Ahmed",
    "Sara",
    "Zaid",
    "John",
    "Karan",
    "Fatima"
}

present_students = {
    "Abu",
    "Ahmed",
    "Sara",
    "Fatima",
    "John"
}


# Question 1

# Total Registered Students


total_register_stu = len(registered_students)
print(f"Total Registered Students : {total_register_stu}")


# Question 2

# Total Present Students

total_preset_stu = len(present_students)
print(f"Present Students : {total_preset_stu}")




# Question 3

# Total Absent Students

# Don't hardcode it.

# Calculate it.

total_absent_stu = total_register_stu - total_preset_stu
print(f"Total Absent Students :- {total_absent_stu}")


# Question 4

# Print the names of all absent students.


absent_stu_name = registered_students - present_students
print(f"Absent Students Name :- {absent_stu_name}")


# Question 5

# Print the attendance percentage.

attendance_percentage = (total_preset_stu / total_register_stu) * 100

print(f"Attendance Percentage Of Class Is :- {attendance_percentage}")


# Question 6

# Print:

# Excellent Attendance

# if attendance ≥ 75%

# Otherwise print:

# Poor Attendance


if attendance_percentage >= 75:
    print("Excellent Attendance!!")
else :
    print("Poor Attendance!!")