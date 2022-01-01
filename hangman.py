"""
Created on Fri Dec 31 05:52:26 2021

@author: alsterra
"""

import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses a word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    lives = 7

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        print('You have ', lives, ' lives left and you used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You have used that letter, try another')

        else:
            print('Invalid character. Please try again')

    # whole berhenti di sini
    if lives == 0:
        print('You died, sorry. The word is ', word)
    else:
        print('You guessed the word ', word, ' :)')

hangman()
