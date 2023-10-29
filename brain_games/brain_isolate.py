#!/usr/bin/env python3
import prompt

name = ''
def welcome_user():
    # Приветствие пользователя
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name         


def game_cycle(game):
    answers_count = 0
    while answers_count < 3:
        welcome_text, question, correct_answer = game()
        if answers_count == 0:
            print(welcome_text)
        print(question)
        user_answer = input('Your answer: ')
        if user_answer == str(correct_answer):
            answers_count += 1
        else:
            print(f'{user_answer} is the wrong answer ;(. The correct answer was {correct_answer}')
            break
    if answers_count == 3:
        print(f'Congratulations, {name}! You answered all questions correctly.')
    else:
        print(f"Let's try again, {name}!")


#def game_result():
    
    
