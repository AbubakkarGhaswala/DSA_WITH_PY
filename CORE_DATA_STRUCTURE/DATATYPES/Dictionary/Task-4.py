# Task - 4 :- Search marks from dic


marks = {
    "Math": 85,
    "Science": 90,
    "English": 75
}

search_sub = input("Enter The Subject Name You Want To See Marks :- ")


find_sub = ""
sub_marks = 0


for subject,mark in marks.items():
    
    if search_sub == subject:
        find_sub = subject
        sub_marks = mark
        break

        

if not find_sub :
    print("Subject Not Found")
else :
    print("Subject Found")
    print(f"{search_sub} {find_sub} {sub_marks}")