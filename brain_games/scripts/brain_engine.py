#!/usr/bin/env python3
# модуль изолированного запуска игр
import prompt


WELCOME = 'Welcome to the Brain Games!'
TURNS = 3


def welcome():
    print(WELCOME)
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_execute(game, task):
    name = welcome()
    print(task)
    answers_count = 0
    while answers_count < TURNS:
        question, correct_answer = game()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')
        if str(user_answer.lower()) == str(correct_answer):
            print('Correct!')
            answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
