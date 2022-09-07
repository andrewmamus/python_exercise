# Write a program that reads the marks of a student and displays PASS or FAIL. It displays FAIL if marks are less than 40 else display PASS.

#  the user will be required to input the score and the if and else condition is been used in this place

marks = int(input("What is the student marks? "))

# condition here
if marks <= 40 :
    print('FAIL')
else:
    print('PASS')