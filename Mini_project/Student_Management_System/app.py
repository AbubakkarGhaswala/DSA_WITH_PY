student_name = []
student_marks = []

while True:
    print("\n==================== Welcome To ========================")
    print("==================== Student Management System ========================")
    print("Press 1 For Add Student")
    print("Press 2 For View All Students")
    print("Press 3 For Search Student")
    print("Press 4 For Find Top Student")
    print("Press 5 For Find Average Marks")
    print("Press 6 For Count Passes/Failed Students")
    print("Press 7 For Exit ")

    user_input = int(input("Enter Your Choice:- "))

    if user_input == 1:
        while True: 
            while True:
                input_for_stu_name = input("Please Enter Student Name :- ").strip()
                if not input_for_stu_name.isalpha():
                    print("Please Enter Valid Name !!")
                else:
                    student_name.append(input_for_stu_name)
                    break 
            
            while True:
                input_for_stu_marks = int(input(f"Please Enter {input_for_stu_name}'s Marks :- "))
                if input_for_stu_marks < 0 or input_for_stu_marks > 100:
                    print("Please Enter Valid Marks Between 0 - 100")
                else:
                    student_marks.append(input_for_stu_marks)
                    break 

            print(f"Information Stored Student Name Is {input_for_stu_name} and Marks Is {input_for_stu_marks}")
            print(f"Here's Updated Record Of Student Name:- {student_name}")
            print(f"Here's Updated Record Of Student Marks:- {student_marks}")
            print("Thank You !!")

            print("If You Want To Add more record type 'yes' or else type 'no' ")
            add_on_input = input("Enter Your Choice:- ").strip().lower()
            
            if add_on_input == "yes":
                print("You've Selected To Add More Records!!\n")
                continue 
            else:
                print("You've Selected to Not Add More Record")
                break 

    elif user_input == 2:
        while True:
            if not student_name or not student_marks:
                print("Please Add Some Records First")
                break
            else:
                print("Here's The Record Of Students !!")
                for t_name, t_marks in zip(student_name, student_marks):
                    print(f"Student Name :- {t_name} , Marks :- {t_marks}")
                print("Thank You !!")
                break
    
    elif user_input == 3:
        while True:
            if not student_name:
                print("Please Add Some Records First")
                break

            search_stu_name = input("Please Enter Student Name To Search :- ").strip()

            if not search_stu_name.isalpha():
                print("Please Enter Valid Student Name !!")
                continue
            
            if search_stu_name in student_name:
                index = student_name.index(search_stu_name)
                name_search = student_name[index]
                marks_search = student_marks[index]

                print("Student Found !! Here's The Details !!")
                print(f"Student Name :- {name_search}")
                print(f"{name_search}'s Marks :- {marks_search}")
                print(" ")
                print("If You Want To Find Another Student Details Then Type 'yes' Else Type 'no'")
                add_on_search = input("Enter Your Choice :- ").lower().strip()

                if add_on_search == 'yes':
                    print("You've Selected To Search Another Student Data!!")
                    continue
                else:
                    break
            else:
                print("Student Not Found !!")
                print("Please Try Again!!")
    elif user_input == 4:
        while True :
            if not student_name or not student_marks:
                print("Please Add Some Data !!")
                break

            else :
                max_marks = student_marks[0]
                top_stu_name = student_name[0]

                for t_name,m_marks in zip(student_name,student_marks):
                    if m_marks > max_marks:
                        max_marks = m_marks
                        top_stu_name = t_name
                
                print(f"Top Student Name Is :- {top_stu_name}\n {top_stu_name}'s Marks Is :- {max_marks}")
                break
    elif user_input == 5:
        while True:
            if not student_marks or len(student_marks) == 1:
                print("Please Enter More Than 1 Record Of Student!!")
                break

            else :

                sum_of_marks = 0
                len_of_marks = len(student_marks)

                for i in student_marks:
                    sum_of_marks = sum_of_marks + i

                avg_marks = sum_of_marks/len_of_marks

                print(f"Total Marks Is :- {sum_of_marks}")
                print(f"Average Marks Is :- {avg_marks}")
                break
    elif user_input == 6:
        while True:
            if not student_marks:
                print("Please Add Some Data !!")
                break
            else :
                pass_stu = 0
                fail_stu = 0

                for i in student_marks:
                    if i >= 35 :
                        pass_stu = pass_stu + 1
                    elif i < 35 :
                        fail_stu = fail_stu + 1

                print(f"Pass Students :- {pass_stu}")
                print(f"Fail Students :- {fail_stu}")
                break

    elif user_input == 7:
        print("Exiting System. Goodbye!")
        break
