# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    boolean = True
    for i in range(0, len(secretWord)):
      if secretWord[i] not in lettersGuessed:
        boolean = False
        break
    
    return boolean



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    currentguess = ''
    for i in range(0,len(secretWord)):
      if secretWord[i] not in lettersGuessed:
        if i > 0 and currentguess[-1] == '_':
          currentguess += ' _'
        else:
          currentguess += '_'
      else:
        currentguess += secretWord[i]
        
    return currentguess


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    allletter = string.ascii_lowercase
    for letter in lettersGuessed:
        allletter = allletter.replace(letter,'')
     
    return allletter
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
    print "-------------"
    totalChances = 8
    chancesLeft = totalChances
    lettersGuessed = []
    availableLetters = getAvailableLetters(lettersGuessed)
    guessedWord = getGuessedWord(secretWord, lettersGuessed)
    winAlready = isWordGuessed(secretWord, lettersGuessed)

    while chancesLeft > 0 and not winAlready:
        print "You have " + str(chancesLeft) + " guesses left."
        print "Available letters: " + availableLetters
        inputletter = raw_input("Please guess a letter: ")
        currentletter = inputletter.lower()
        if currentletter in lettersGuessed:
            print "Oops! You've already guessed that letter: " + guessedWord
            print "-------------"
            continue
        else:
            lettersGuessed.append(currentletter)
            availableLetters = getAvailableLetters(lettersGuessed)
            if currentletter in secretWord:
                guessedWord = getGuessedWord(secretWord, lettersGuessed)
                winAlready = isWordGuessed(secretWord, lettersGuessed)
                print "Good guess: " + guessedWord
                print "-------------"
            else:
                print "Oops! That letter is not in my word: " + guessedWord
                print "-------------"
                chancesLeft -= 1

    if winAlready == True:
        print "Congratulations, you won!"
    elif chancesLeft == 0:
        print "Sorry, you ran out of guesses. The word was " + str(secretWord) + "."


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
