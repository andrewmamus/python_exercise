# Write a program that reads the students ‘registration number & his GPA and then print a message according to class of his GPA.

# Note we need to get te registration number and GPA before we print

registNum = int(input("Please type your registration number "))
# GPA should be float because most of GPA are decimal
gpa = float(input("Enter your GPA: "))

print(registNum, " your GPA is ", gpa)