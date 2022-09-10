# Write a program that reads the rate of pay per hour of an employee and reads the hours worked using while-loop statement. Calculates the gross wage and display the output on the screen.

counter = 1
days_worked = int(input("Enter days you work: "))
amount_per_hour = int(input("Enter amount paid per hour"))
gross = 0
while counter <= days_worked:
    hours = int(input("How many hours did you work today? "))
    gross += hours * amount_per_hour
    counter += 1

print("The gross wage is: ", gross)