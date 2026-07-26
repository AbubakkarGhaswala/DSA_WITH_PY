# student_name = ["Abu", "Ali", "Ahmed"]
# student_marks = [85, 70, 95]

# max_marks = student_marks[0]
# top_stu = ""


# for i,t_name in zip(student_marks,student_name):
#     if i > max_marks:
#         max_marks = i
#         top_stu = t_name
    

# print(max_marks)
# print(top_stu)

marks = [88,95,92,86,67]

sum_of_marks = 0
len_of_marks = len(marks)


for i in marks:
    sum_of_marks = sum_of_marks + i
avg_marks = sum_of_marks/len_of_marks

print(f"Sum OF Marks is {sum_of_marks}")
print(avg_marks)