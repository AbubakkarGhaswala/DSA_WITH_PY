students = {
    "Abu": {
        "Math": 85,
        "Science": 90,
        "English": 75
    },
    "Ali": {
        "Math": 30,
        "Science": 25,
        "English": 40
    },
    "Ahmed": {
        "Math": 95,
        "Science": 88,
        "English": 92
    }
}

total_stu = 0
total_avg_marks = 0

passed_stu = 0
fail_stu = 0

stu_name_list = []
avg_stu_list = []

for stu_name in students:
    total_marks = 0
    count_sub = 0
    is_passed = True  
    
    print(f"Student Name :- {stu_name}")   
    stu_name_list.append(stu_name) 
    
    for sub, mark in students[stu_name].items():
        print(f"Subject : {sub}  || marks : {mark}")
        total_marks = total_marks + mark
        count_sub = count_sub + 1
        
        if mark <= 35:
            is_passed = False

    print(f"Total Marks :- {total_marks}")
    
    average_marks = total_marks / count_sub
    print(f"Average Marks :- {average_marks:.2f}")
    avg_stu_list.append(average_marks)
    total_stu = total_stu + 1
    total_avg_marks = total_avg_marks + average_marks

    if average_marks <= 35:
        is_passed = False
    
    if is_passed == True:
        print("Result: Pass\n")
        passed_stu = passed_stu + 1
    else:
        print("Result: Fail\n")
        fail_stu = fail_stu + 1
    print("---------------------------------")


class_avg = total_avg_marks / total_stu

print("---------------------------------")
print(f"Total Students: {total_stu}\n")
print(f"Overall Class Average :- {class_avg:.2f}\n")

highest_stu_name = stu_name_list[0]
highest_stu_avg = avg_stu_list[0]


for st_name , avg_st in zip(stu_name_list,avg_stu_list):
    if avg_st > highest_stu_avg:
        highest_stu_avg = avg_st
        highest_stu_name = st_name

print("---------------------------------")

print(f"Top Student Name Is :- {highest_stu_name}\n")
print(f"And {highest_stu_name}'s Average Marks Is {highest_stu_avg}\n")


print("---------------------------------")

print(f"Passed Student :- {passed_stu}\n")
print(f"Failed Student :- {fail_stu}")

print("---------------------------------")
print("Thank You For Using!!!")