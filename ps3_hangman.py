# Hangman game

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    return set(secretWord).issubset(lettersGuessed)


def getGuessedWord(secretWord, lettersGuessed):
    value = ""
    string = ""
    for i in secretWord:
        if i in lettersGuessed:
            value = i + " "
        else:
            value = "_ "
        string += value
    return string
def getAvailableLetters(lettersGuessed):
    import string
    lettersA = list(string.ascii_lowercase)
    b = [ x for x in lettersA if not x in lettersGuessed ] 
    return ''.join(b)
def hangman(secretWord):
 
    print("Welcome to the game, Hangman!") 
    print("I am thinking of a word that is", str(len(secretWord)), " letters long.") 
    print("-------------") 
    guessLeft = 8 
    lettersGuessed=[]
    while guessLeft > 0 and not isWordGuessed(secretWord, lettersGuessed):
        print("You have " + str(guessLeft) + " guesses left.")
        print("Available letters: " + str(getAvailableLetters(lettersGuessed)))
        guess = (str(input("Please guess a letter: "))).lower()
        if guess not in lettersGuessed:
            lettersGuessed.append(guess)
            if guess in secretWord:
                print('Good guess: ', str(getGuessedWord(secretWord, lettersGuessed)))
                print("------------")
            else:
                guessLeft -= 1
                print("Oops! That letter is not in my word: ", str(getGuessedWord(secretWord, lettersGuessed)))
                print("------------")
        else:
            print("Oops! You've already guessed that letter: ", str(getGuessedWord(secretWord, lettersGuessed)))
            print("------------")
    if isWordGuessed(secretWord, lettersGuessed): 
        print("Congratulations, you won!") 
    else:
        print("Sorry, you ran out of guesses. The word was", str(secretWord)) 

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
