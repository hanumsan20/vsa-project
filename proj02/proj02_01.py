# Name: Santosh
# Date: 6/19/2017

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

name = raw_input("Enter your name: ")
age = int(raw_input("Enter your age: "))
birthday = raw_input("Has your birthday happened this year? Enter Y or N: ")
if birthday == "Y":
    year = 2017
    year_100 = (2017 - age) + 100
    num = 2017
    while num < (year_100 + 1):
        print str(num)
        num = num + 1
else:
    year = 2016
    year_100 = (2017 - age) + 99
    num = 2016
    while num < (year_100 + 1):
        print str(num)
        num = num + 1
# Calculates the year that the user will be 100
# TO DO: write for or while loop that adds one year to year each time and stops at the year that the user will be 100

