print("---------- Divide 2 Numbers ----------")

try:
    print("Database Connected..")

    a = int(input("Enter First value :- "))
    b = int(input("Enter Second value :- "))

    result = a / b

    print(f"Your ans is :- {result}")

except ZeroDivisionError:
    print("User You Can Not Divide A Number With Zero")

except ValueError:
    print("Invalid Input")

except Exception:
    print("Oops!! Something Went Wrong..")

finally:
    print("Database Connection Closed..")
    print("GoodByeee....")