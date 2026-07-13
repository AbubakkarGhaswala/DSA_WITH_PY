# Hello Everyone And Welcome To day we are going to check the grades of the student according to the marks they have got using conditions (if , elif , else)


marks = int(input("Enter Your Marks :- "))

if marks < 0 or marks > 100:
    print("Enter Valid Marks")
elif marks >= 90 and marks <= 100:
    print("A")
elif marks >=80 and marks <= 89:
    print("B")
elif marks >=70 and marks < 80:
    print("C")
elif marks >= 60 and marks < 70:
    print("D")
elif marks >=40 and marks < 60 :
    print("E")
elif marks < 40:
    print("Fail")


# Task 5 Done !!
