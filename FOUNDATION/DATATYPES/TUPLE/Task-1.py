students = (
    ("Abu", 85),
    ("Ali", 91),
    ("Sara", 78),
    ("Zoya", 95)
)


# Your mission
# Print:
# Abu : 85
# Ali : 91
# Sara : 78
# Zoya : 95
# Find the student with the highest marks.

# Expected output:

# Top Student: Zoya
# Marks: 95



for name,mark in students:
    print(f"{name} : {mark}")



top_stu = ""
highest_marks = 0


for top_name,high_mark in students:
    if high_mark > highest_marks:
        top_stu = top_name
        highest_marks = high_mark


print(f"Top Student Name Is :- {top_stu}")
print(f"{top_stu}'s Marks Is :- {highest_marks}")