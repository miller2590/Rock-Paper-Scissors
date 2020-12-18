#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 13:30:13 2020

@author: gage
"""

import random

while True:
    
    pc_pic = random.choice(['Rock', 'Paper', 'Scissors'])

    player_pic = input("Rock, Paper, Scissors shoot! \nChoice:").capitalize()

    # This covers a tie game
    if player_pic == pc_pic:
        print(f'{pc_pic}! Tie game!')
        
    # This covers player_pic Rock
    elif player_pic == 'Rock' and pc_pic == 'Paper':
        print(f'{pc_pic}! I win!')
     
    elif player_pic == 'Rock' and pc_pic == 'Scissors':
        print(f'{pc_pic}! You win!')
        
    # This covers player_pic Paper
    
    elif player_pic == 'Paper' and pc_pic == 'Scissors':
        print(f'{pc_pic}! I win!')
        
    elif player_pic == 'Paper' and pc_pic == 'Rock':
        print(f'{pc_pic}! You win!')
    
    # This covers player_pic Scissors
    
    elif player_pic == 'Scissors' and pc_pic == 'Paper':
        print(f'{pc_pic}! You win!')
    
    elif player_pic == 'Scissors' and pc_pic == 'Rock':
        print(f'{pc_pic}! I win!')
        
     # Countinue game or quit
     
    game_state = input("""Would you like to play again?
                       'y' or 'n': """).lower()
    if game_state == 'n':
        break
    else:
        print('Game on!')