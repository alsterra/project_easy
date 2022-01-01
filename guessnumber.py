# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 04:38:26 2021

@author: alsterra
"""

import random

def guess(n):
    random_number = random.randint(1,n)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {n}: "))
        if guess < random_number:
            print("Sorry, you guessed too low")
        elif guess > random_number:
            print("Wow, you guessed too high")
    print(f"Horray, good. You are not that idiot. You can guess {guess} correctly.")

guess(10)