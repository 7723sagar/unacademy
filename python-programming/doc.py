"""
This is a docstring
=================================================================
This is the program to find the current age of the student
by inputting Year of Birth and Present year.
Ask the User name also!
"""

#ask user name
name = input("What's your name?")

#ask year of birth
YoB = int(input("What's Year of Birth? "))

#ask present year
year = int(input("What's the recent year? "))

#calculate age
age = year - YoB

#print the age
print(name + " you are " + str(age) + " years old!")
