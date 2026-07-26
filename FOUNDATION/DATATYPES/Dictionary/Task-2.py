#Task 2 — Total and Average Marks

marks = {
    "Math": 85,
    "Science": 90,
    "English": 75
}


count_of_sub = 0

sum_of_marks = 0

for i in marks:
    count_of_sub = count_of_sub + 1

    
    sum_of_marks = sum_of_marks + marks[i]


avg_marks = round(sum_of_marks / count_of_sub,2)


print(f"Total Marks :- {sum_of_marks}")

print(f"Average Of Marks :- {avg_marks}")