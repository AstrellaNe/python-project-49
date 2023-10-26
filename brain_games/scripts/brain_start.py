#!/usr/bin/env python3
# Главный скрипт для вызова всех игр

import prompt
import brain_games.games.brain_calc as brain_calc
import brain_games.games.brain_even as brain_even

games = { # словарь, чтобы можно было добавить в будущем много других игр
    '1': brain_even.main,
    '2': brain_calc.main,
    }

def welcome_user(): # приветствие пользователя
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_choice():
    non_digit_choice = 0
    while non_digit_choice < 3:
        choice = prompt.string('''Choose a game: 
    Print "1" for "Even or Odd"
    Print "2" for "Calculator": ''') # пробелы сознательно сделаны
        if choice.isdigit():
            game_function = games.get(choice)
            if game_function:
                correct_answer = game_function()
                user_answer = input('Your answer: ')
                return choice, correct_answer, user_answer
            else:
                print('Invalid choice. Please choose a valid game number.')
        else:
            print('Digits only!')
            non_digit_choice += 1
    print('You have exceeded the maximum number of invalid choices.')
    return None, None, None



def game_cycle(): #  один цикл игры
    choice, correct_answer, user_answer = game_choice()
    if correct_answer is not None and user_answer is not None:
        if user_answer == str(correct_answer):
            print('Correct!')
        else:
            print(f'Wrong! The correct answer was: {correct_answer}')
    else:
        print(f'{user_answer} is the wrong answer ;(. The correct answer was {correct_answer}')
        

def goofy_check(user_answer): 
    while game_choice = '2':
        if user_answer = int():
        return int(user_answer)
    else:
        return 'non_digit'


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    answers_count = 0 # счетчик правильных ответов
    for turn in range(3): # 3 раунда на любую игру
        choice, correct_answer, user_answer = game_choice() 
        # получаем из фунции game_choice() переменные
        if correct_answer is not None and user_answer is not None:
        # сравниваем ответы если не None
            if user_answer == str(correct_answer):
            # приводим ответы к str 
                print('Correct!')
                answers_count += 1
            else:
                print(f'''{user_answer} is the wrong answer ;(. The correct answer was {correct_answer}
Let's try again, {name}!''')
                return
        

    if answers_count == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")



if __name__ == '__main__':
    main()
