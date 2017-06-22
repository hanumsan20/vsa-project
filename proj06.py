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

    word_in_list = []

    final_word_reveal = []

    for letter in word:
        word_in_list.append(letter)

    # (TO BE DELETED):.
    print "Current word: " + str(word_in_list)
    # (TO BE DELETED)^


    print "\nWelcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(word_in_list)) + " letters long!"
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    guesses = 8
    for var in range(0,9):
        print "\nYou have " + str(guesses) + " guesses remaining!"
        guess_letter = raw_input("Please guess a letter: ").lower()

        if guess_letter == word[0]:
            print "\nGreat guess!"
            alphabet.remove(str(guess_letter))
            word_in_list.remove(str(guess_letter))
            final_word_reveal.append(str(guess_letter))
            print "Available letters: " + str(alphabet)

            if word_in_list == []:
                print "\nYou finished the game! Hooray!"

            #(TO BE DELETED):
            print "Current word: " + str(word_in_list)
            #(TO BE DELETED)^

        elif guess_letter == word[1]:
            print "\nGreat guess!"
            alphabet.remove(str(guess_letter))
            word_in_list.remove(str(guess_letter))
            final_word_reveal.append(str(guess_letter))
            print "Available letters: " + str(alphabet)

            if word_in_list == []:
                print "\nYou finished the game! Hooray!"

            #(TO BE DELETED):
            print "Current word: " + str(word_in_list)
            #(TO BE DELETED)^


        elif guess_letter == word[2]:
            print "\nGreat guess!"
            alphabet.remove(str(guess_letter))
            word_in_list.remove(str(guess_letter))
            final_word_reveal.append(str(guess_letter))
            print "Available letters: " + str(alphabet)

            if word_in_list == []:
                print "\nYou finished the game! Hooray!"

            #(TO BE DELETED):
            print "Current word: " + str(word_in_list)
            #(TO BE DELETED)^


        elif guess_letter == word[3]:
            print "\nGreat guess!"
            alphabet.remove(str(guess_letter))
            word_in_list.remove(str(guess_letter))
            final_word_reveal.append(str(guess_letter))
            print "Available letters: " + str(alphabet)

            if word_in_list == []:
                print "\nYou finished the game! Hooray!"

            #(TO BE DELETED):
            print "Current word: " + str(word_in_list)
            #(TO BE DELETED)^


        elif guess_letter == word[4]:
            print "\nGreat guess!"
            alphabet.remove(str(guess_letter))
            word_in_list.remove(str(guess_letter))
            final_word_reveal.append(str(guess_letter))
            print "Available letters: " + str(alphabet)

            if word_in_list == []:
                print "\nYou finished the game! Hooray!"

            #(TO BE DELETED):
            print "Current word: " + str(word_in_list)
            #(TO BE DELETED)^


        elif guess_letter == word[5]:
            print "\nGreat guess!"
            alphabet.remove(str(guess_letter))
            word_in_list.remove(str(guess_letter))
            final_word_reveal.append(str(guess_letter))
            print "Available letters: " + str(alphabet)

            if word_in_list == []:
                print "\nYou finished the game! Hooray!"

            #(TO BE DELETED):
            print "Current word: " + str(word_in_list)
            #(TO BE DELETED)^

        elif guess_letter == word[6]:
            print "\nGreat guess!"
            alphabet.remove(str(guess_letter))
            word_in_list.remove(str(guess_letter))
            final_word_reveal.append(str(guess_letter))
            print "Available letters: " + str(alphabet)

            if word_in_list == []:
                print "\nYou finished the game! Hooray!"

            #(TO BE DELETED):
            print "Current word: " + str(word_in_list)
            #(TO BE DELETED)^

        elif guess_letter == word[7]:
            print "\nGreat guess!"
            alphabet.remove(str(guess_letter))
            word_in_list.remove(str(guess_letter))
            final_word_reveal.append(str(guess_letter))
            print "Available letters: " + str(alphabet)

            if word_in_list == []:
                print "\nYou finished the game! Hooray!"

            #(TO BE DELETED):
            print "Current word: " + str(word_in_list)
            #(TO BE DELETED)^

        # elif guess_letter == word[8]:
        #     print "\nGreat guess!"
        #     alphabet.remove(str(guess_letter))
        #     word_in_list.remove(str(guess_letter))
        #     print "Available letters: " + str(alphabet)
        #
        #     if word_in_list == []:
        #         print "\nYou finished the game! Hooray!"
        #
        #     #(TO BE DELETED):
        #     print "Current word: " + str(word_in_list)
        #     #(TO BE DELETED)^



        elif guess_letter != word[0] or guess_letter != word[1] or guess_letter != word[2] or guess_letter != word[3] or guess_letter != word[4] or guess_letter != word[5] or guess_letter != word[6] or guess_letter != word[7]:
            print "\nThat is not correct. Please try again!"
            alphabet.remove(str(guess_letter))
            print "Available letters: " + str(alphabet)
            guesses = guesses - 1

    # if player runs out of guesses:
    print "\nI am sorry but you have ran out of guesses!"
    print "The word was: " + str(word) + "!"

        # else:
        #     print "That is not correct. Please try again!"
        #     alphabet.remove(str(guess_letter))
        #     print "Available letters: " + str(alphabet)
        #     guesses = guesses - 1



hangman()