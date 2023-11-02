#!/usr/bin/env python3
# модуль изолированного запуска игр
import prompt


def welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def game_cycle(game):
    answers_count = 0
    while answers_count < 3:
        welcome_text, question, correct_answer = game()
        if answers_count == 0:
            print(welcome_text)
        print(question)
        user_answer = input('Your answer: ')
        if str.lower(user_answer) == str(correct_answer):
            print('Correct!')
            answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            break
    if answers_count == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")