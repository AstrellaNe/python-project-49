#!/usr/bin/env python3
# Главный скрипт для вызова всех игр

import prompt
import brain_games.games.brain_calc 
import brain_games.games.brain_even 

def welcome_user(): #приветствие пользователя
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_choice(): #выбор игры и проверка на ввод данных
    non_digit_choice = 0
    exit_game = False
    while non_digit_choice < 3:
        game_choice = prompt.string('Choose a game: Print "1" for "Even or Odd" or "2" for "Calculator": ')
        if game_choice == '1':
            brain_games.games.brain_even.main()
            user_answer = input('Your answer: ')
            return str(user_answer)
        elif game_choice == '2':
            brain_games.games.brain_calc.main()
        else:
            print('Invalid choice. Please choose 1 or 2.')
            non_digit_choice += 1
            if non_digit_choice == 3:
                print('You have exceeded the maximum number of invalid choices.')
                break
            

    

def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    answers_count = 0
    for turn in range(3):
        game_choice()
        user_answer = input('Your answer: ')
        return str(user_answer)
    if user_answer == game_choice():
        
    
    
    
    if game_choice == '3':    
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
        return 


if __name__ == '__main__':
    main()
