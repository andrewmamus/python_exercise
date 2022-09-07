# Exercise One 
# Write a program to find the area of a circle, given that the area of a circle is pi*r²

# We need to import the Math module
import math

# variables and we need to request for the radius for the user
pi = math.pi
r = int(input("Please Enter the radius: "))

Area = pi*(r**2)

print(Area)