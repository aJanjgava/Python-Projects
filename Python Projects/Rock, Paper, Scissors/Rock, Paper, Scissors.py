"""
    Rock, Paper, Scissors
"""

import random

exit = False

while exit == False:
    options = ['rock', 'paper', 'scissors']
    user_input = input('Choose rock, paper, scissors or exit: ')
    computer_choice = random.choice(options)

    if user_input == 'exit':
        print('Game over!')
        exit = True

    if user_input == 'rock':
        if computer_choice == 'rock':
            print('Your input is rock')
            print('Computer input is rock')
            print('It is a tie!')

        elif computer_choice == 'paper':
            print('Your input is rock')
            print('Computer input is paper')
            print('Computer wins!')

        elif computer_choice == 'scissors':
            print('Your input is rock')
            print('Computer input is scissors')
            print('You win!')

    elif user_input == 'paper':
        if computer_choice == 'rock':
            print('Your input is paper')
            print('Computer input is rock')
            print('You win!')

        elif computer_choice == 'paper':
            print('Your input is paper')
            print('Computer input is paper')
            print('It is tie!')

        elif computer_choice == 'scissors':
            print('Your input is paper')
            print('Computer input is scissors')
            print('Computer wins!')

    elif user_input == 'scissors':
        if computer_choice == 'rock':
            print('Your input is scissors')
            print('Computer input is rock')
            print('Computer wins!')

        elif computer_choice == 'paper':
            print('Your input is scissors')
            print('Computer input is paper')
            print('You win!')

        elif computer_choice == 'scissors':
            print('Your input is scissors')
            print('Computer input is scissors')
            print('It is tie!')