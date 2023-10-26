#!/usr/bin/env python3
# Главный скрипт для вызова всех игр

import prompt
import brain_games.games.brain_calc as brain_calc
import brain_games.games.brain_even as brain_even
import brain_games.games.brain_comdiv as brain_comdiv

games = { # словарь, чтобы можно было добавить в будущем много других игр
    '1': brain_even.main,
    '2': brain_calc.main,
    '3': brain_comdiv.main,
    }

def welcome_user(): # приветствие пользователя
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_choice():
    non_digit_choice = 0 # счетчик неверного ввода выбора игры
    while non_digit_choice < 3:
        choice = prompt.string('''Choose a game: 
    Print "1" for "Even or Odd"
    Print "2" for "Calculator"
    Print "3" for "Common Divisor": ''') # пробелы сознательно сделаны
        if choice.isdigit():
            game_function = games.get(choice)
            if game_function:
                correct_answer = game_function()
                user_answer = input('Your answer: ')
                return choice, correct_answer, user_answer, non_digit_choice
            else:
                print('Invalid choice. Please choose a valid game number.')
        else:
            print('Digits only!')
            non_digit_choice += 1 
    print('''You have exceeded the maximum number of invalid choices.
Sorry, we are quiting the game. Try again next time, {name}!''')
    return None, None, None, non_digit_choice



def game_cycle(): #  один цикл игры
    choice, correct_answer, user_answer, non_digit_choice = game_choice()
    if choice == None:
        return False # передаем в main переменную для обрыва игры после ошибок ввода
    elif non_digit_choice == 3:
        print(f'''Sorry,{name}, too many mistakes ;(.
We end the game. Let's try again next time!''')
        return False
    elif correct_answer is not None and user_answer is not None:
        if user_answer == str(correct_answer):
                print('Correct!')
                return True
        else:
            print(f'{user_answer} is the wrong answer ;(. The correct answer was {correct_answer}')
            return False
    else:
        print(f'{user_answer} is the wrong answer ;(. The correct answer was {correct_answer}')
        return False
        

def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    answers_count = 0 # счетчик правильных ответов
    
    
    while answers_count < 4:
   # 3 раунда на любую игру     
        game_cycle
        if game_cycle() == True:  
            answers_count += 1       
        else:
            return   

    if answers_count == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")
        return


if __name__ == '__main__':
    main()
