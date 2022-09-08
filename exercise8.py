# Write a program that calculates the sum as well as the average score of 10 students in a class using for-loop statement.

sum = 0
average = 0
# first we need the input of the user but 10 times
for i in range(1, 11):
    sum+= int(input("Enter score: "))
average = sum/10

print('The sum of the score is ', sum, 'and the average is ', average)