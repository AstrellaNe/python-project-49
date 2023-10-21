#!/usr/bin/env python3
# Главный скрипт для вызова всех игр

import prompt
import brain_games.games.brain_calc 
import brain_games.games.brain_even 

def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def main():
    print('Welcome to the Brain Games!')
    game_choice = prompt.string('Choose a game: 1 - Even or Odd or 2 - Calculator: ')
    if game_choice == '1':
        brain_games.games.brain_even.main()
    elif game_choice == '2':
        brain_games.games.brain_calc.main()
    else:
        print('Invalid choice. Please choose 1 or 2.')

if __name__ == '__main__':
    main()
