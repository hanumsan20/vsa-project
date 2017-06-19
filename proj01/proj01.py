# Name: Santosh
# Date: 6/19/2017
#
# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.
#
# If you complete extensions, describe your extensions here!


# to 'restart' the program
print "\n"
def again():
    print "\n"
    playagain = raw_input("Would you like to play again? Please enter 'yes' or 'no': ").lower()
    if playagain == "yes":
        print "\n"
        main()
    elif playagain == "no":
        quit()
    else:
        print "I did not get that. Please try again"
        print "\n"
        again()

# main program

def main():
    name = raw_input("What is your first name? ").title()
    age = raw_input("What is your age? [Please enter as a number, i.e. 21] ")
    # allows program to be run any year! (not just 2017)
    currentyear = raw_input("What year are you currently in right now, " + name + "? ")


    if int(age) < 100:

    # birthday
        birthday = raw_input("Have you already had a birthday this year? Enter 'yes' or 'no': ").lower()

        if birthday == "yes":
            newyear = (int(currentyear) - int(age)) + 100
        elif birthday == "no":
            newyear = (int(currentyear) - int(age)) + 99

    print "\n"

    if int(age) < 100:
        print name + " will turn 100 in the year " + str(newyear) + "!"
    elif int(age) == 100:
        print name + " is already 100 years old! Congratulations!"
    # if you already turned over 100 years old -- it will calculate what year you turned 100
    elif int(age) > 100:
        turnedage = (int(currentyear) - int(age)) + 100
        print name + " is over " + str(age) + " years old, which means they turned 100 in the year " + str(turnedage) + "!"



    if int(age) >= 18:
        print name + " is allowed to see G, PG, PG-13, and R rated movies!"
    elif int(age) >= 13 and int(age) < 18:
        print name + " is allowed to see G, PG, and PG-13 rated movies!"
    elif int(age) <= 12:
        print name + " is allowed to see G and PG rated movies!"
    else:
        print "Please enter your age again."

    again()


main()

