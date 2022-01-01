# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 05:17:56 2021

@author: alsterra
"""

import random

def computer_guess(n):
    low = 1
    high = n
    user_input = ""
    while user_input != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        user_input = input(f"Is {guess} to high (H), too low (L), or correct (C)? ").lower()
        if user_input == 'h':
            high = guess - 1
        elif user_input == 'l':
            low = guess + 1
    print(f"Yay! The computer is not that idiot too! It can guess {guess} correctly.")
    

computer_guess(10)