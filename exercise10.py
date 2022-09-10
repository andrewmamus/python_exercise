#Write a program that reads the score of 10 subjects of 20 students. Calculte the sum of scores, and display the names and average.

# this program requires nexted loop you can use while or for loop
output = ""
for i in range(1, 21):
    name = input("Enter student name: ")
    stu_sum = 0
    for j in range(1,11):
        score = int(input("Enter Score: "))
        stu_sum += score
    average = stu_sum/10
    output += name + " Score: " + str(stu_sum)+ " Average: " + str(average) + "\n" #The plus sign is called concatination and the str() is use to convert the integer to string in other to be able to cocantinate the integers
print(output)
    