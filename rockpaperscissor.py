# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 05:31:48 2021

@author: alsterra
"""

import random

def play():
    user = input("Choose 'r' for rock, 'p' for paper, 's' for scissor: ")
    computer = random.choice(["r","p","s"])
    
    if user == computer:
        return "tie"
    
    if is_win(user, computer):
        return "You won!"
    
    return "You lost! Wasted!"

def is_win(player,opponent):
    if(player == "r" and opponent == "s") or (player == "s" and opponent == "p") \
        or (player == "p" and opponent == "r"):
        return True
    
print(play())