marks = [78, 92, 65, 88, 71]


total = 0



heighest_marks = marks[0]

lowest_marks = marks[0]


for i in marks:
    total = total + i

    if i > heighest_marks:
        heighest_marks = i
    elif i < lowest_marks:
        lowest_marks = i


avg_marks = total/len(marks)


print(f"Total Marks :- {total}")
print(f"Average Marks :- {avg_marks}")
print(f"Heighest Marks :- {heighest_marks}")
print(f"Lowest Marks :- {lowest_marks}")