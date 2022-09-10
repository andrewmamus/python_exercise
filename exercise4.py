# Write a program that reads the students ‘registration number & his GPA and then print a message according to class of his GPA.

# Note we need to get te registration number and GPA before we print

registNum = int(input("Please type your registration number "))
# GPA should be float because most of GPA are decimal
gpa = float(input("Enter your GPA: "))
if gpa >= 3.5:
    grade = "Distinction"
elif gpa >= 3.0:
    grade = "Upper Credit"
elif gpa >= 2.5:
    grade = "Lower Credit"
elif gpa >= 2.0:
    grade = "Pass"
else:
    grade = "Fail"
print(registNum, " your GPA is ", gpa, "and your grade is ", grade)