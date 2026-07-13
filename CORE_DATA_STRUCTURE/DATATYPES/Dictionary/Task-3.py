#Task 3 — Highest Subject

marks = {
    "Math": 85,
    "Science": 90,
    "English": 75
}

highest_sub = ""
highest_marks = 0

for subject,mark in marks.items():
    if mark > highest_marks:
        highest_marks = mark
        highest_sub = subject


print(f"Highest Subject Is {highest_sub} and Highest Marks Is {highest_marks}")


