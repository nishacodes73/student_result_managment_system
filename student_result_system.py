print("------------------------------------------")
print("***** STUDENT RESULT MANAGEMENT SYSTEM *****")
print("------------------------------------------")

# Student information
na = input("Enter your name: ").strip()
print("Student name:", na.upper())

print("------------------------------------------")

age = int(input("Enter your age: "))
print("Student's age:", age)

print("------------------------------------------")
print("***** ENTER YOUR SUBJECT MARKS *****")

# Subject marks
Eng = float(input("Enter your English marks: "))
chem = float(input("Enter your Chemistry marks: "))
phy = float(input("Enter your Physics marks: "))

print("------------------------------------------")

# Validate marks
if  Eng < 0 or Eng > 100 or chem < 0 or chem > 100 or phy < 0 or phy > 100:
    print("Invalid marks! Marks must be between 0 and 100.")

else:
    # Calculate total and percentage
    Total_marks = Eng + chem + phy
    print("Total marks:", Total_marks)

    per = (Total_marks / 300) * 100
    print(f"Percentage: {per:.2f}%")
    print("Percentage data type:", type(per))

    print("------------------------------------------")

    # Grade and result
    if Eng < 33 or chem < 33 or phy < 33:
        print("Grade: F")
        print("Result: FAIL")

    elif per >= 90:
        print("Grade: A+")
        print("Result: PASS")

    elif per >= 75:
        print("Grade: A")
        print("Result: PASS")

    elif per >= 60:
        print("Grade: B")
        print("Result: PASS")

    elif per >= 40:
        print("Grade: C")
        print("Result: PASS")

    else:
        print("Grade: F")
        print("Result: FAIL")

    print("------------------------------------------")
    print("***** THANK YOU *****")
    print("------------------------------------------")