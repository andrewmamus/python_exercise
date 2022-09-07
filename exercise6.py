# 6. Write an appropriate IF – THEN – ELSE statement for the following:
# Test the value of the variable hours. If hours is less than or equal to 40, assign 4.50 to pay and assign “Regular” to the variable 
# status. If pay exceeds 40, assign 6.25 to pay and assign “overtime” to status.


# lets get the hours from the users
hours = int(input("Enter hours: "))
pay, status = 0, 0
if hours <= 40:
    pay = 4.50
    status = "Regular"
else:
    pay = 6.25
    status = "overtime"
