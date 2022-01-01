# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 13:16:06 2021

@author: alsterra
"""

import math
import random


class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # we wall all players to get their next move given a game
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # akan di cek bahwa ini merupakan nilai yg benar, dengan cast
            # ke integer, dan jika tidak akan muncul invalid
            # jika spot juga tidak tersedia, maka akan invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True  # jika berhasil, yaudah sip
            except ValueError:
                print('Invalid square. Try again.')
        return val


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            # randomly choose one
            square = random.choice(game.available_moves())
        else:
            # get the square based off the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'  # the other player

        # first we want to check if the previous move is a winner
        # this is our base case
        if state.current_winner == other_player:
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)
                    }

        elif not state.empty_squares():  # no empty square
            return {'position': None, 'score': 0}

        if player == max_player:
            # each score should maximize (be larger)
            best = {'position': None, 'score': -math.inf}
        else:
            # each score should minimize
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move, player)
            # step 2: recurese using minimax to simulate a game after making that move
            # now, we alternate players
            sim_score = self.minimax(state, other_player)
            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            # otherwise this will get messed up from the recursion
            sim_score['position'] = possible_move
            # step 4: update the dictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score  # replace best
            else:  # but minimize the other player
                if sim_score['score'] < best['score']:
                    best = sim_score  # replace best

        return best