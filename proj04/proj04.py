# Name:
# Date:

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""

from string import whitespace

def main():
    word_input = raw_input("Please enter a word: ").lower()

    word_input_list = []

    for letter in word_input:
        word_input_list.append(letter)

    # str(word_input).replace(' ', '')

    if word_input_list == word_input_list[::-1]:
        print str(word_input) + " is a palindrome! Congratulations!"
        playAgain = raw_input("\nWould you like to play again? Yes or No? ").lower()
        if playAgain == "yes" or playAgain == "y" or playAgain == "yeah" or playAgain == "yup" or playAgain == "yea":
            main()
        else:
            quit()
    elif word_input_list != word_input_list[::-1]:
        print str(word_input) + " is NOT a palindrome! I am sorry!"
        playAgain = raw_input("\nWould you like to play again? Yes or No? ").lower()
        if playAgain == "yes" or playAgain == "y" or playAgain == "yeah" or playAgain == "yup" or playAgain == "yea":
            main()
        else:
            quit()

main()