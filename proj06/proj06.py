# Name:
# Date:


# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.


    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

def hangman():
    word = choose_word(wordlist)
    print "\nWelcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(word)) + " letters long!"
    print word
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    guesses = 8
    for var in range(0,9):
        print "\nYou have " + str(guesses) + " guesses remaining!"
        # print "Available letters: " + str(alphabet)
        guess_letter = raw_input("Please guess a letter: ").lower()

        if guess_letter == word[0]:
            print "Great guess!"
            alphabet.remove(str(guess_letter))
            print "Available letters: " + str(alphabet)


        elif guess_letter == word[1]:
            print "Great guess!"
            alphabet.remove(str(guess_letter))
            print "Available letters: " + str(alphabet)


        elif guess_letter == word[2]:
            print "Great guess!"
            alphabet.remove(str(guess_letter))
            print "Available letters: " + str(alphabet)


        elif guess_letter == word[3]:
            print "Great guess!"
            alphabet.remove(str(guess_letter))
            print "Available letters: " + str(alphabet)


        elif guess_letter == word[4]:
            print "Great guess!"
            alphabet.remove(str(guess_letter))
            print "Available letters: " + str(alphabet)


        elif guess_letter == word[5]:
            print "Great guess!"
            alphabet.remove(str(guess_letter))
            print "Available letters: " + str(alphabet)
            guesses = guesses - 1

        elif guess_letter == word[6]:
            print "Great guess!"
            alphabet.remove(str(guess_letter))
            print "Available letters: " + str(alphabet)


        elif guess_letter == word[7]:
            print "Great guess!"
            alphabet.remove(str(guess_letter))
            print "Available letters: " + str(alphabet)



        else:
            print "That is not correct. Please try again!"
            alphabet.remove(str(guess_letter))
            print "Available letters: " + str(alphabet)
            guesses = guesses - 1



hangman()