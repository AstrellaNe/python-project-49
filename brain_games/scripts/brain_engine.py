#!/usr/bin/env python3
# модуль изолированного запуска игр
import prompt

WELCOME = 'Welcome to the Brain Games!'
print(WELCOME)
NAME = prompt.string('May I have your name? ')
print(f'Hello, {NAME}!')


def game_cycle(game):  # добавлен аргумент NAME
    answers_count = 0
    while answers_count < 3:
        TASK, (question, correct_answer) = game()
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
        print(f'Congratulations, {NAME}!')
    else:
        print(f"Let's try again, {NAME}!")
